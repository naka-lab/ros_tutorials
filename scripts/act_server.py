#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import rospy
import actionlib
from ros_tutorials.msg import *

action_server = None

def callback( goal ):
    print(goal)    
    r = rospy.Rate(1)
    sequence = [0, 1]
    
    for i in range(1, goal.order+1):
        if action_server.is_preempt_requested():
            print("stop")
            break
        
        sequence.append( sequence[i]+sequence[i-1] )
        action_server.publish_feedback( ActTutorialFeedback(sequence) )
        print(sequence)
        r.sleep()

    action_server.set_succeeded( ActTutorialResult( sequence ) )        


def main():
    global action_server
    rospy.init_node("action_server")
    action_server = actionlib.SimpleActionServer("ros_tutorial_action", ActTutorialAction, execute_cb=callback, auto_start=False)
    action_server.start()
    rospy.spin() 
    
    
if __name__ == "__main__":
    main()
 
