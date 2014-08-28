#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import random


def pubvel():
    rospy.init_node('publish_velocity')
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1000)
    r = rospy.Rate(2)
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = random.random()
        msg.angular.z = random.uniform(-1, 1)
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()
        rospy.loginfo(msg)


if __name__ == '__main__':
    try:
        pubvel()
    except rospy.ROSInterruptException:
        pass
