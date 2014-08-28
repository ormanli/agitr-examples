#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from std_srvs.srv import Empty

if __name__ == '__main__':
    try:
        rospy.init_node('set_bg_color')

        rospy.wait_for_service('clear')

        rospy.set_param('background_r', 255)
        rospy.set_param('background_g', 255)
        rospy.set_param('background_b', 0)

        clearClient = rospy.ServiceProxy('/clear', Empty)

        clearClient()
    except rospy.ROSInterruptException:
        pass
