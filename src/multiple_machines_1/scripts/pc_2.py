#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    data_pc2 = data.data * 2
    rospy.loginfo("Received: %d, Publishing: %d", data.data, data_pc2)
    pub.publish(data_pc2)

def listener():
    rospy.init_node('PC_Yusril')
    rospy.Subscriber('data_pc1', Int32, callback)
    global pub
    pub = rospy.Publisher('data_pc2', Int32, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()
