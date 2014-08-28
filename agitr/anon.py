#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy

if __name__ == '__main__':
    try:
        rospy.init_node('anon', anonymous=True)
        r = rospy.Rate(1)

        while not rospy.is_shutdown():
            rospy.loginfo('This message is from ' + rospy.get_name())

            r.sleep()
    except rospy.ROSInterruptException:
        pass
