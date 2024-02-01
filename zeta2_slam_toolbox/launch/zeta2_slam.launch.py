import launch
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import launch_ros
import os

def generate_launch_description():
    zeta_slam_toolbox_pkg = launch_ros.substitutions.FindPackageShare(package='zeta2_slam_toolbox').find('zeta2_slam_toolbox')

    # Path to the additional launch files
    display_launch_file_path = os.path.join(zeta_slam_toolbox_pkg, 'launch/display.launch.py')
    slam_toolbox_launch_file_path = os.path.join(zeta_slam_toolbox_pkg, 'launch/offline.launch.py')

    return launch.LaunchDescription([
        # Include the display launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(display_launch_file_path)
        ),

        # Include the SLAM toolbox launch file
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_toolbox_launch_file_path)
        ),
    ])