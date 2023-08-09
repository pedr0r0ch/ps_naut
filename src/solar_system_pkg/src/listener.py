#!/usr/bin/python3

import rospy
import tf2_ros
import geometry_msgs.msg
from geometry_msgs.msg import TransformStamped


class Listener:
    def __init__(self, headerName, childName):
        self.__headerName = headerName
        self.__childName = childName
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)

    def listening(self):
        try:
            transform = self.tf_buffer.lookup_transform(self.__headerName, self.__childName, rospy.Time())
            self.process_transform(transform)
        
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            pass

    def process_transform(self, transform):
        translation = transform.transform.translation
        rotation = transform.transform.rotation

if __name__ == '__main__':
    rospy.init_node('listener_solar_system')
    listener1 = Listener("sun", "earth")
    listener2 = Listener("earth", "moon")
    #listener3 = Listener("sun", "mars")


    
    rate = rospy.Rate(1)  # frequência de atualização em Hz
    
    while not rospy.is_shutdown():
        listener1.listening()
        listener2.listening()
        #listener3.listening()

        rate.sleep()

