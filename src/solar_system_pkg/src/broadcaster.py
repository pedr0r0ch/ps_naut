#!/usr/bin/python3

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
import tf_conversions
import geometry_msgs.msg
import math
import time


#Frame Estático. Vamos assumir que a estrela será o frame fixo/estatico
class FixedFrame():
    def __init__(self, nameChild):
        self.nameChild = nameChild
        self.br = tf2_ros.StaticTransformBroadcaster()

    def publishStaticTransform(self):

            t = TransformStamped()
            t.header.frame_id = "world"
            t.child_frame_id = self.nameChild
            t.header.stamp = rospy.Time.now()
            
            t.transform.translation.x = 1
            t.transform.translation.y = 1
            t.transform.translation.z = 1.0

            t.transform.rotation.x = 0
            t.transform.rotation.y = 0
            t.transform.rotation.z = 1
            t.transform.rotation.w = 0

            self.br.sendTransform(t)



class myBroadcaster():
    def __init__(self, nameChild, nameHeader, orbit, angle):
        self.__angle = angle
        self.__orbit = orbit
        self.__nameChild = nameChild
        self.__nameHeader = nameHeader
        self.__br = tf2_ros.TransformBroadcaster()


    def publishBr(self):
        
        transf = TransformStamped()
            
        transf.header.frame_id = self.__nameHeader
        transf.child_frame_id = self.__nameChild
        transf.header.stamp = rospy.Time.now()

        #variável que vamos utilizar para modelagem de movimento
        x = rospy.Time.now().to_sec()
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, self.__angle)

        transf.transform.translation.x = self.__orbit*math.cos(x)
        transf.transform.translation.y = self.__orbit*math.sin(x)
        transf.transform.translation.z = 0

        transf.transform.rotation.x = q[0]
        transf.transform.rotation.y = q[1]
        transf.transform.rotation.z = q[2]
        transf.transform.rotation.w = q[3]        

        self.__br.sendTransform(transf)

    

if __name__ == "__main__":
    rospy.init_node("solar_system")
    
    fx = FixedFrame("sun")
    fx.publishStaticTransform()
    rospy.Rate(1)

    angle = 0
    while not rospy.is_shutdown():
        
        earthOrbit = rospy.get_param('Earth/orbit', default=0) #as orbitas estao definidas no servidor de parametros
        moonOrbit = rospy.get_param('Moon/orbit', default=0)
        marsOrbit = rospy.get_param('Mars/orbit', default=0)

        #a = myBroadcaster("sun", "mars", marsOrbit, angle)
        #a.publishBr()

        b = myBroadcaster("sun", "earth", earthOrbit, angle)
        b.publishBr()

        c = myBroadcaster("earth", "moon", moonOrbit, angle)
        c.publishBr()
        
        angle += 0.1  # Incrementar o ângulo de rotação
        if angle >= 2 * math.pi:
            angle = 0.0
        
        time.sleep(1/24)# questoes de visualizacao