#!/bin/bash
# Script that synchronizes the robot’s time while connecting to SSH

# Set the robot's username and host
ROBOT_USER="zeta"
ROBOT_HOST="10.42.0.1"
ROBOT_PASSWORD="1"

# Get the client's current time in 'YYYY-MM-DD HH:MM:SS' format.
LOCAL_TIME=$(date +"%Y-%m-%d %H:%M:%S")

# Connect to the robot using SSH and send a command to set the robot’s time.
# Use the entered password for the sudo command.
sshpass -p 1 ssh -t $ROBOT_USER@$ROBOT_HOST -o StrictHostKeyChecking=no "echo $ROBOT_PASSWORD | sudo -S date -s '$LOCAL_TIME'"