#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist

forward = True
pub = None


def toggleForward(req):
    global forward
    forward = not forward

    rospy.loginfo(
        'Now sending %s command', 'forward' if forward else 'rotate')

    msg = Twist()
    msg.linear.x = 1.0 if forward else 0.0
    msg.angular.z = 0.0 if forward else 1.0
    pub.publish(msg)

    return []


if __name__ == '__main__':
    try:
        rospy.init_node('pubvel_toggle')

        s = rospy.Service('toggle_forward', Empty, toggleForward)

        pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1000)

        rospy.loginfo('pubvel_toggle started')

        r = rospy.Rate(2)
        while not rospy.is_shutdown():
            r.sleep()
            rospy.spin()

    except rospy.ROSInterruptException:
        pass
