#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy


def hello():
    rospy.init_node('hello_ros')
    rospy.loginfo('Hello, ROS!')


if __name__ == '__main__':
    try:
        hello()
    except rospy.ROSInterruptException:
        pass
