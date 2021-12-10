# ENPM662-Project2

## Moveit

This package depends on the robot_2 package. Hence make sure that robot_2 package is in the same workspace and compiled.<br>

- Copy the moveit package in the workspace
- Open terminal and navigate to the workspace
- Build the package: catkin build moveit
- Source the setup.bash in the devel folder: source ./devel/setup.bash
- Open a terminal and navigate to the workspace and source the setup.bash from and then run: roslaunch moveit gazebo.launch
- Open another terminal and navigate to the workspace and source the setup.bash from and then run: roslaunch moveit move_group.launch
- Open another terminal and navigate to the workspace and source the setup.bash from and then run: roslaunch moveit moveit_rviz.launch 
- Click on Add in the left panel and add motionplanning. A planning window will pop up at the left panel.
- Select the start and end goal from the dropdown
- Press plan and execute. It will take about 10 seconds to find the path. Note that this will not move the arm in gazebo as the controllers are not setup.