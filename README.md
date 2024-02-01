

## First time you must complete zeta2_bringup

- https://github.com/zetabank-devteam/zeta2_edu_devel.git

-------------

```bash
# slam_toolbox
sudo apt install ros-humble-slam-toolbox -y

# cartographer
sudo apt install ros-humble-cartographer -y
sudo apt install ros-humble-cartographer-ros -y

# navigation
sudo apt install ros-humble-navigation2 -y
sudo apt install ros-humble-nav2-bringup -y
```

```bash
source /opt/ros/humble/setup.bash
source ~/zeta_ws/install/setup.bash

cd ~/zeta_ws/src
git clone https://github.com/zetabank-devteam/zeta2_edu_autonomous.git

cd ~/zeta_ws
colcon build --packages-select zeta2_navigation zeta2_slam_toolbox zeta2_cartographer

source /opt/ros/humble/setup.bash
source ~/zeta_ws/install/setup.bash

ros2 launch zeta2_bringup zeta2_bringup.launch.py # if, mc, control, odom, making tf, scan

ros2 launch zeta2_bringup zeta_joy.launch.py

ros2 launch zeta2_cartographer zeta2_cartographer.launch.py
ros2 run nav2_map_server map_saver_cli -f carto_seongsu


ros2 launch zeta2_slam_toolbox zeta2_slam_toolbox.launch.py
ros2 run nav2_map_server map_saver_cli -f slam_toolbox_seongsu


ros2 launch zeta2_navigation zeta2_navigation.launch.py



source /opt/ros/humble/setup.bash
source ~/zeta_ws/install/setup.bash
ros2 launch zeta2_description display.launch.py
```
