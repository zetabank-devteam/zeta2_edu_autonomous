

## First time you must complete zeta2_bringup

- https://github.com/zetabank-devteam/zeta2_edu_devel.git

-------------

```bash
# bringup
sudo apt install ros-humble-tf-transformations -y
sudo apt install python3-pip -y
sudo pip3 install transforms3d 
sudo apt install ros-humble-robot-localization -y


# description
sudo apt install ros-humble-joint-state-publisher-gui -y
sudo apt install ros-humble-xacro -y

# slam
sudo apt install ros-humble-slam-toolbox -y


# navigation
sudo apt install ros-humble-navigation2 -y
sudo apt install ros-humble-nav2-bringup -y

# uron
sudo apt install nlohmann-json3-dev
```

```bash
source /opt/ros/humble/setup.bash
source ~/zeta_ws/install/setup.bash

cd ~/zeta_ws
```

```bash
colcon build --packages-select zeta2_navigation zeta2_slam_toolbox
colcon build --packages-select zeta2_uron
colcon build --packages-select zeta2_bringup


source ~/.bashrc

# ros2 launch zeta2_bringup zeta_if.launch.py # interface board -> imu, sonar
# ros2 launch zeta2_bringup zeta_mc.launch.py # motor board -> motor
# ros2 launch zeta2_bringup control.launch.py # input motor
# ros2 launch zeta2_bringup odometry.launch.py # odom
ros2 launch zeta2_bringup zeta2_bringup.launch.py # if, mc, control, odom
ros2 launch zeta2_uron test.launch

ros2 topic pub --once /robot_command std_msgs/msg/String "data: '{\"MoveDelta\": 0.1}'"
ros2 topic pub --once /robot_command std_msgs/msg/String "data: '{\"MoveDelta\": 0.45}'"

ros2 topic pub --once /robot_command std_msgs/msg/String "data: '{\"TurnDelta\": 0.524}'"
ros2 topic pub --once /robot_command std_msgs/msg/String "data: '{\"TurnDelta\": 0.785}'"
ros2 topic pub --once /robot_command std_msgs/msg/String "data: '{\"TurnDelta\": 1.57}'"


ros2 topic pub --once /robot_command std_msgs/msg/String "data: '{\"Stop\": 1}'"

ros2 launch zeta2_bringup zeta_joy.launch.py


ros2 launch zeta2_bringup launch_robot.launch.py # making tf

ros2 launch ldlidar ldlidar.launch.py serial_port:=/dev/ttyS0 lidar_frame:=base_scan # scan

# ros2 launch zeta2_description display.launch.py # rviz

ros2 launch zeta2_slam_toolbox zeta2_slam.launch.py


ros2 service call /slam_toolbox/save_map slam_toolbox/srv/SaveMap "{name: {data: 'seongsu'}}"


ros2 launch zeta2_navigation navigation.launch.py
ros2 launch zeta2_navigation navigation_test.launch.py



source /opt/ros/humble/setup.bash
source ~/zeta_ws/install/setup.bash
ros2 launch zeta2_description display.launch.py
```
