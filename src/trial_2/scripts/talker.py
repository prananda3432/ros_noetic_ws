#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

data_reset = False

def callback(data):
    rospy.loginfo("Data: %s", data.data)
    data_buffer = data.data
    print(data_buffer)
    if data_buffer == 1:
        data_reset = True
    else:
        data_reset = False

def get_data_reset():
    rospy.spin()

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('data_1', Int16, queue_size=10)
    rospy.Subscriber("Reset", Bool, callback)
    rate = rospy.Rate(10)
    test_1 = 0
    while not rospy.is_shutdown():
        if data_reset == True:
            test_1 = 0
        else:
            test_1 += 1
        #rospy.loginfo(test_1)
        pub.publish(test_1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
        get_data_reset()
    except rospy.ROSInterruptException:
        pass
