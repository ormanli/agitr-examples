#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import random

pub = None


def commandVelocityReceived(msgIn):
    msgOut = Twist()
    msgOut.linear.x = -msgIn.linear.x
    msgOut.angular.z = -msgIn.angular.z
    pub.publish(msgOut)


if __name__ == '__main__':
    try:
        rospy.init_node('reverse_velocity')
        pub = rospy.Publisher('turtle1/cmd_vel_reversed', Twist,
                              queue_size=1000)
        rospy.Subscriber('turtle1/cmd_vel', Twist,
                         commandVelocityReceived, queue_size=1000)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
