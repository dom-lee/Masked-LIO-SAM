# Masked LIO-SAM : LiDAR Inertial Odometry in Dynamic Environments

Team 25: Andrew Wei, Anurekha Ravikumar, Dongmyeong Lee, Manohar Bhat, Qi Dai\
Contact authors: awei@umich.edu, anurekha@umich.edu, domlee@umich.edu, manubhat@umich.edu, qidai@umich.edu \
ROB 530 Mobile Robotics Final Project - University of Michigan - Ann Arbor


## Abstract
Simultaneous Localization and Mapping (SLAM) is not robust in dynamic environments, where objects move and cause changes in the surroundings, its effectiveness is limited. It is particularly challenging to use SAM methods that depend on visual or point cloud data, as the dynamic objects can be registered in multiple scans. To address this issue, we propose a method that combines Sparsely Embedded Convolutional Detection (SECOND) and LiDAR Inertial Odometry Smoothing And Mapping. Our approach involves masking out the point cloud features detected by SECOND in the Velodyne scan. Then we occlude the features and update it to LIO-SAM to help it develop the map and state estimation. Our experimental results demonstrate the effectiveness of our approach, which achieves good? accuracy in localization compared to the original LIO-SAM method. By enabling SLAM to work more effectively in dynamic environments, this could enhance the safety and reliability of various autonomous systems.

<p align='center'>
    <img src="./doc/masked-lio-sam_overview.gif" alt="drawing" width="800"/>
</p>

<p align='center'>
    <img src="./doc/masked-lio-sam_birdeye.gif" alt="drawing" width="800"/>
</p>


## System architecture
<p align='center'>
    <img src="./doc/masked-lio-sam_pipeline.png" alt="drawing" width="800"/>
</p>


## Dependency
- [ROS](http://wiki.ros.org/ROS/Installation) (Tested with Noetic)
```
sudo apt-get install -y ros-noetic-navigation
sudo apt-get install -y ros-noetic-robot-localization
sudo apt-get install -y ros-noetic-robot-state-publisher
sudo apt-get install -y ros-noetic-jsk-rviz-plugins
sudo apt-get install -y ros-noetic-vision-msgs
```

- [gtsam](https://gtsam.org/get_started/) (Georgia Tech Smoothing and Mapping library)
```
sudo add-apt-repository ppa:borglab/gtsam-release-4.0.3
sudo apt install libgtsam-dev libgtsam-unstable-dev
```


## Install
Use the following commands to download an compile the package
```
cd ~/catkin_ws
git clone https://github.com/dom-lee/Masked-LIO-SAM.git src
git submodule update --init --recursive
cd ..
catkin_make
```


## Run the package
1. Run the launch file (Masked-LIO-SAM & SECOND):
```
roslaunch lio_sam run.launch
roslaunch multiple-object-tracking kitti-raw.launch
```
2. Play existing bag files:
```
rosbag play <example>.bag
```


## Dataset
The KITTI raw dataset is used to evaluate Masked LIO-SAM.
- KITTI (raw) Dataset: (https://www.cvlibs.net/datasets/kitti/raw_data.php)
    - Need to convert into bag file with `kitti2bag.py` located in `LIO-SAM/config/doc/kitti2bag` folder.
- **2011_09_30_drive_0028:** [[Google Drive](https://drive.google.com/drive/folders/1gJHwfdHCRdjP7vuT556pv8atqrCJPbUq?usp=sharing)] (provided by https://github.com/TixiaoShan/LIO-SAM)


## Evaluate Trajectories
Use this script to combine bagfiles from LIO-SAM and Masked LIO-SAM outputs for plotting them together using EVO (https://github.com/MichaelGrupp/evo). 
Edit `scene` inside `eval/traj_eval.py` to the corresponding KITTI scene, then run:
```
cd eval/
python traj_eval.py 
```
