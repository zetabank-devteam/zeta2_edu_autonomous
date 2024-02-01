from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, FindExecutable, PathJoinSubstitution
import launch_ros
import os

def generate_launch_description():
    zeta2_cartographer_pkg = launch_ros.substitutions.FindPackageShare(package='zeta2_cartographer').find('zeta2_cartographer')
    zeta2_cartographer_config = os.path.join(zeta2_cartographer_pkg, 'config')
    zeta2_cartographer_config_file = os.path.join(zeta2_cartographer_config, 'zeta2_ldlidar.lua')
    rviz_config_dir = os.path.join(zeta2_cartographer_pkg, 'rviz', 'zeta2_cartographer.rviz')

    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{
                'configuration_directory': zeta2_cartographer_config,
                'configuration_basename': zeta2_cartographer_config_file,
            }],
            remappings=[
                ('scan', 'scan'),
                ('odom', 'odom')
            ]
        ),
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_occupancy_grid_node',
            arguments=['-resolution', '0.05']
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            output='screen'
        ),
    ])