#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose


def poseMessageReceived(msg):
    rospy.loginfo(rospy.get_caller_id() + ' position=(' + str(msg.x)
                  + ',' + str(msg.y) + ') direction=' + str(msg.theta))


if __name__ == '__main__':
    try:
        rospy.init_node('subscribe_to_pose')
        rospy.Subscriber('turtle1/pose', Pose, poseMessageReceived,
                         queue_size=1000)

        rospy.spin()
    except rospy.ROSInterruptException:
        pass
