#!/usr/bin/env python
from __future__ import print_function, unicode_literals
from ros_tutorials.srv import *
import rospy

def add(req):
    print( req.a, req.b, req.a + req.b)
    return SrvTutrialResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('servise_server')
    s = rospy.Service('add', SrvTutrial, add)
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
