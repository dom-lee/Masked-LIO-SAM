# Masked LIO-SAM : LiDAR Inertial Odometry in Dynamic Environments

Team 25: Andrew Wei, Anurekha Ravikumar, Dongmyeong Lee, Manohar Bhat, Qi Dai\
Contact authors: awei@umich.edu, anurekha@umich.edu, domlee@umich.edu, manubhat@umich.edu, qidai@umich.edu \
ROB 530 Mobile Robotics Final Project - University of Michigan - Ann Arbor

## Abstract
Simultaneous Localization and Mapping (SLAM) is not robust in dynamic environments, where objects move and cause changes in the surroundings, its effectiveness is limited. It is particularly challenging to use SAM methods that depend on visual or point cloud data, as the dynamic objects can be registered in multiple scans. To address this issue, we propose a method that combines Sparsely Embedded Convolutional Detection (SECOND) and LiDAR Inertial Odometry Smoothing And Mapping. Our approach involves masking out the point cloud features detected by SECOND in the Velodyne scan. Then we occlude the features and update it to LIO-SAM to help it develop the map and state estimation. Our experimental results demonstrate the effectiveness of our approach, which achieves good? accuracy in localization compared to the original LIO-SAM method. By enabling SLAM to work more effectively in dynamic environments, this could enhance the safety and reliability of various autonomous systems.

## Dependency
- [ROS](http://wiki.ros.org/ROS/Installation) (Tested with noetic distro)

## Dataset
The KITTI raw dataset is used to evaluate Masked LIO-SAM.
- KITTI (raw) Dataset: (https://www.cvlibs.net/datasets/kitti/raw_data.php)

## Code Download
```
git clone https://github.com/dom-lee/Masked-LIO-SAM/
```

## Masked LIO-SAM 
```
cd LIO-SAM/
roslaunch lio_sam run.launch /
```
## in another terminal 
```
roslaunch multiple-object-tracking kitti-raw.launch /
```
## in another terminal 
```
rosbag play <path_to_bag_file>
```

## Evaluate Trajectories
Use this script to combine bagfiles from LIO-SAM and Masked LIO-SAM outputs for plotting them together using EVO (https://github.com/MichaelGrupp/evo). 
Edit `scene` inside `eval/traj_eval.py` to the corresponding KITTI scene, then run:
```
cd eval/
python traj_eval.py 
```
