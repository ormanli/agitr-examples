#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
import random

if __name__ == '__main__':
    try:
        rospy.init_node('publish_velocity')
        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1000)

        max_vel = rospy.get_param('~max_vel', 'nan')

        if max_vel == 'nan':
            rospy.logfatal('Could not get parameter ~max_vel')
            exit(1)

        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            msg = Twist()
            msg.linear.x = max_vel * random.random()
            msg.angular.z = random.uniform(-1, 1)
            rospy.loginfo(msg)
            pub.publish(msg)
            r.sleep()

    except rospy.ROSInterruptException:
        pass
