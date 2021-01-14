#!/usr/bin/env python
from __future__ import print_function, unicode_literals
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('listener2', anonymous=True)

    while not rospy.is_shutdown():
        data = rospy.wait_for_message( "chatter", String )
        print( data.data )
        
if __name__ == '__main__':
    main()
