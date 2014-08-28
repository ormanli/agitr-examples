#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from turtlesim.srv import Spawn
import math

if __name__ == '__main__':
    try:
        rospy.init_node('spawn_turtle')

        spawnClient = rospy.ServiceProxy('spawn', Spawn)

        success = spawnClient(2, 2, math.pi / float(2), 'Leo')

        rospy.loginfo(success)

    except rospy.ROSInterruptException:
        pass
