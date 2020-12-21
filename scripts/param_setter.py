#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import rospy

def main():
    global param
    rospy.init_node("param_setter")
    
    while not rospy.is_shutdown():
        param = raw_input("input parameter ->")
        param = float(param)
        rospy.set_param( "/param_tutrial/param", param )
        
if __name__ == "__main__":
    main()
