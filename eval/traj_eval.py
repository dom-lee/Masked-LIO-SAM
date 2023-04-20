import os 
from rosbags.rosbag1 import Reader
from rosbags.rosbag1 import Writer
from rosbags.serde import deserialize_cdr, ros1_to_cdr, cdr_to_ros1, serialize_cdr

scene = '0047'

combined_file = 'traj_eval/combined_lio-sam_' + scene  + '_traj_eval_data.bag'
lio_file = 'traj_eval/lio-sam_' + scene  + '_traj_eval_data.bag'
masked_file = 'traj_eval/masked_lio-sam_' + scene  + '_traj_eval_data.bag'

# topics = ['/odometry/gps', '/odometry/imu_incremental', '/lio_sam/mapping/odometry_incremental']
msg_dict = {}
connection_dict = {}

if os.path.exists(combined_file):
    os.remove(combined_file)

# create reader instance
with Writer(combined_file) as writer:
    with Reader(lio_file) as reader_lio:
        for connection, timestamp, rawdata in reader_lio.messages():
            # if connection.topic in topics:
            topic = connection.topic

            if topic not in msg_dict.keys():
                msg_dict[topic] = []
                connection_dict[topic] = writer.add_connection(topic, connection.msgtype, latching=1)

            msg = deserialize_cdr(ros1_to_cdr(rawdata, connection.msgtype), connection.msgtype)
            write_msg = cdr_to_ros1(serialize_cdr(msg, connection.msgtype), connection.msgtype)
            msg_dict[topic].append((connection_dict[topic], timestamp, write_msg))
                

    with Reader(masked_file) as reader_masked:
        for connection, timestamp, rawdata in reader_masked.messages():
            # if connection.topic in topics:
            topic = '{}_masked'.format(connection.topic)

            if topic not in msg_dict.keys():
                msg_dict[topic] = []
                connection_dict[topic] = writer.add_connection(topic, connection.msgtype, latching=1)

            msg = deserialize_cdr(ros1_to_cdr(rawdata, connection.msgtype), connection.msgtype)
            write_msg = cdr_to_ros1(serialize_cdr(msg, connection.msgtype), connection.msgtype)
            msg_dict[topic].append((connection_dict[topic], timestamp, write_msg))

    for write_topics in msg_dict.values():
        for tup in write_topics:
            write_connection, timestamp, write_msg = tup
            writer.write(write_connection, timestamp, write_msg)