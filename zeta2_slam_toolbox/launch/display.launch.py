import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    zeta_slam_toolbox_pkg = launch_ros.substitutions.FindPackageShare(package='zeta2_slam_toolbox').find('zeta2_slam_toolbox')
    default_rviz_config_path = os.path.join(zeta_slam_toolbox_pkg, 'rviz/nav2.rviz')
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                            description='Absolute path to rviz config file'),
        rviz_node
    ])