
# Zeta Edu Autonomous

## zeta2 bringup을 먼저 완료하세요.

- [zeta2_bringup](https://github.com/zetabank-devteam/zeta2_edu_devel.git)

-------------

## 필수 패키지 설치

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
## zeta_edu_autonomous 패키지 설치
```bash
source /opt/ros/humble/setup.bash

cd ~/zeta_ws/src
git clone https://github.com/zetabank-devteam/zeta2_edu_autonomous.git

cd ~/zeta_ws
colcon build --packages-select zeta2_navigation zeta2_slam_toolbox zeta2_cartographer

source ~/zeta_ws/install/setup.bash
```

## slam tool box 매핑

1. zeta2_bringup을 실행한다.
```bash
ros2 launch zeta2_bringup zeta2_bringup.launch.py # if, mc, control, odom, making tf, scan
```
2. 조이스틱 조작을 위해 zeta_joy를 실행한다.
```bash
ros2 launch zeta2_bringup zeta_joy.launch.py
```
3. zeta_slam_toolbox를 실행한다.
```bash
ros2 launch zeta2_slam_toolbox zeta2_slam_toolbox.launch.py
```
3. rviz 화면을 보고 지도를 다 그리면 지도를 저장한다.
```bash
## ros2 run nav2_map_server map_saver_cli -f {원하는 지도 이름}
## 예시
ros2 run nav2_map_server map_saver_cli -f slam_toolbox_seongsu
```



## cartographer 매핑

1. zeta2_bringup을 실행한다.
```bash
ros2 launch zeta2_bringup zeta2_bringup.launch.py # if, mc, control, odom, making tf, scan
```
2. 조이스틱 조작을 위해 zeta_joy를 실행한다.
```bash
ros2 launch zeta2_bringup zeta_joy.launch.py
```
3. zeta_cartographer를 실행한다.
```bash
ros2 launch zeta2_cartographer zeta2_cartographer.launch.py
```
3. rviz 화면을 보고 지도를 다 그리면 지도를 저장한다.
```bash
## ros2 run nav2_map_server map_saver_cli -f {원하는 지도 이름}
## 예시
ros2 run nav2_map_server map_saver_cli -f carto_seongsu
```


## navigation2 실행


```bash
ros2 launch zeta2_navigation zeta2_navigation.launch.py

source /opt/ros/humble/setup.bash
source ~/zeta_ws/install/setup.bash
```
