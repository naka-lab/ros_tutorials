#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import rospy
import actionlib
from ros_tutorials.msg import *


def feedback( fb ):
    print("feedback", fb )


def main():
    rospy.init_node("action_client")
    action_client = actionlib.SimpleActionClient( "ros_tutorial_action", ActTutorialAction )
    action_client.wait_for_server()
    
    goal = ActTutorialGoal()
    goal.order = 10
    
    action_client.send_goal( goal, feedback_cb=feedback )
    action_client.wait_for_result()
    result = action_client.get_result()
    print("result", result.sequence)
    
    
    
if __name__ == "__main__":
    main()
