#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import sys
import rospy
from ros_tutorials.srv import *

def main():
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    rospy.init_node('srvise_client' )
    rospy.wait_for_service('add')
    add = rospy.ServiceProxy('add', SrvTutrial)
    print( x, y, add(x, y) )


if __name__ == "__main__":
    main()


 
