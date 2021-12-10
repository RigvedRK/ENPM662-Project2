# ENPM662-Project2

## robot_2

#### Arm Movement

- Copy the robot_2 package in the workspace
- Open terminal and navigate to the workspace
- Build the package: catkin build robot_2
- Source the setup.bash in the devel folder: source ./devel/setup.bash
- Launch the package: roslaunch robot_2 gazebo.launch
- Open another terminal, navigate to the workspace and source the setup from devel
- Run the script to demonstrate the movement of the arm: rosrun robot_2 arm.py
- You can also program the arm to go to specific position by uncommenting line 28,29 and commenting all lines after that. Put the desired values of angles in the function parameters.

#### Kinematic Validation

- Run the kinematics.py present in the scripts folder of the package in python3
- The code will print the transformation matrices for the configuration mentioned in the techinical document and the rotation matrix for the computed angles in IK validation.
- You can validate the output for other configurations as well by substituing the desired values in the final transformation matrix. Use line 32 as referance. 