#!/usr/bin/env python2
import rospy
from std_msgs.msg import Float64
import time
import numpy as np

joint_0 = rospy.Publisher('/robot_2/joint_0_controller/command', Float64, queue_size=1, latch=True)
joint_1 = rospy.Publisher('/robot_2/joint_1_controller/command', Float64, queue_size=1, latch=True)
joint_2 = rospy.Publisher('/robot_2/joint_2_controller/command', Float64, queue_size=1, latch=True)
joint_3 = rospy.Publisher('/robot_2/joint_3_controller/command', Float64, queue_size=1, latch=True)
joint_4 = rospy.Publisher('/robot_2/joint_4_controller/command', Float64, queue_size=1, latch=True)
joint_5 = rospy.Publisher('/robot_2/joint_5_controller/command', Float64, queue_size=1, latch=True)

def moveToAngle(theta0=0,theta1=0,theta2=0,theta3=0,theta4=0,theta5=0,):
    joint_0.publish(theta0)
    joint_1.publish(theta1)
    joint_2.publish(theta2)
    joint_3.publish(theta3)
    joint_4.publish(theta4)
    joint_5.publish(theta5)
    # rospy.spin()
    # r.sleep()

rospy.init_node('arm_control')
r = rospy.Rate(10)

# Validation Angles
# moveToAngle(1.57,-1.57,0,3.14,0,0)
# time.sleep(5)

moveToAngle(-2,2.7,-2.5,0,0,0)
time.sleep(5)
moveToAngle(2,2.7,-2.5,0,0,0)
time.sleep(5)
moveToAngle(3,1.5,0,0,0,0)
time.sleep(5)
moveToAngle(-3,1.5,0,0,0,0)
time.sleep(5)
moveToAngle(-3,1.5,-1.5,0,0,0)
time.sleep(5)
moveToAngle(3,1.5,-1.5,0,0,0)
time.sleep(5)
moveToAngle(3,1.5,-3,0,0,0)
time.sleep(5)
moveToAngle(-3,1.5,-3,0,0,0)
time.sleep(5)
moveToAngle(-3,0,0,0,0,0)
time.sleep(5)
moveToAngle(3,0,0,0,0,0)
time.sleep(5)
moveToAngle(3,0,-1.5,0,0,0)
time.sleep(5)
moveToAngle(-3,0,-1.5,0,0,0)
time.sleep(5)