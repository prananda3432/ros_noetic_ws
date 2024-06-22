#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

def callback(data):
    data_pc3 = data.data - 2 # ubah data dari pc yang disubscribe mau di apaain, entah di kali, di kurang, di bagi, dll
    rospy.loginfo("Received: %d, Publishing: %d", data.data, data_pc3)
    pub.publish(data_pc3)

def listener():
    rospy.init_node('PC_3') #ubah disni jadi 'PC_Nanda'
    rospy.Subscriber('data_pc2', Int32, callback) # ubah disini jadi data_pc yang mau di subsribe
    global pub
    pub = rospy.Publisher('data_pc3', Int32, queue_size=10) # uabh disini jadi data_pc yang mau di publish nama topic nya
    rospy.spin()

if __name__ == '__main__':
    listener()
