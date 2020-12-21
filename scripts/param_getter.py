#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import rospy

param = 10
def main():
    global param
    rospy.init_node("param_getter")
    rospy.set_param( "/param_tutrial/param", param )
    
    r = rospy.Rate(1)
    while not rospy.is_shutdown():
        param = rospy.get_param( "/param_tutrial/param" )
        print(param)
        r.sleep()
        
if __name__ == "__main__":
    main()
