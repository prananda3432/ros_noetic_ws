#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

def callback(data):
    rospy.loginfo("Data: %s", data.data)
    get_data_1 = data.data
    pub_reset = rospy.Publisher("Reset", Bool, queue_size=10)
    if get_data_1 >= 100:
        pub_reset.publish(1)
    else:
        pub_reset.publish(0)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("data_1", Int16, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
