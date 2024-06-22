#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int32

def callback(data):
    rospy.loginfo("Received data from topic data_pc3: %d", data.data)

def talker():
    pub = rospy.Publisher('data_pc1', Int32, queue_size=10)
    rospy.init_node('PC_Nanda')
    rospy.Subscriber('data_pc3', Int32, callback)
    rate = rospy.Rate(1) # 10hz
    data = 0
    while not rospy.is_shutdown():
        if data == 100:
            data = 0
        else:
            data += 1
        rospy.loginfo(data)
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
