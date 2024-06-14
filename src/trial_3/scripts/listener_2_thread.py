#!/usr/bin/env python

import rospy
import threading
from rosserial_arduino.msg import Adc
from std_msgs.msg import String

def adc_callback(data):
    rospy.loginfo("Received ADC data: adc0=%d, adc1=%d, adc2=%d, adc3=%d, adc4=%d, adc5=%d" % 
                  (data.adc0, data.adc1, data.adc2, data.adc3, data.adc4, data.adc5))

def chatter_callback(data):
    rospy.loginfo("Received message: %s" % data.data)

def adc_listener():
    rospy.Subscriber("adc", Adc, adc_callback)
    rospy.spin()

def chatter_listener():
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('arduino_listener', anonymous=True)

    adc_thread = threading.Thread(target=adc_listener)
    chatter_thread = threading.Thread(target=chatter_listener)

    adc_thread.start()
    chatter_thread.start()

    adc_thread.join()
    chatter_thread.join()
