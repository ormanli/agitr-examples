#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy

if __name__ == '__main__':
    try:
        rospy.init_node('count_and_log')
        r = rospy.Rate(10)
        i = 0
        while not rospy.is_shutdown():
            rospy.logdebug('Counted to ' + str(i))

            if i % 3 == 0:
                rospy.loginfo(str(i) + ' is divisible by 3.')
            if i % 5 == 0:
                rospy.logwarn(str(i) + ' is divisible by 5.')
            if i % 10 == 0:
                rospy.logerr(str(i) + ' is divisible by 10.')
            if i % 20 == 0:
                rospy.logfatal(str(i) + ' is divisible by 20.')

            r.sleep()
            i += 1
    except rospy.ROSInterruptException:
        pass
