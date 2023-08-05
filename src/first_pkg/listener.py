#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Vector3
from std_msgs.msg import Float32

def callback_status(data):
    rospy.loginfo(rospy.get_caller_id() + "Mensagem recebida! -> '%s'", data.data)


def callback_vector3_linear(data):
    rospy.loginfo(rospy.get_caller_id() + "Mensagem recebida! -> '%f, %f, %f'", data.x, data.y, data.z)
    topico1 = rospy.Publisher('topico_modulo_VL', Float32, queue_size=10) #crindo um novo topico
    mensagemTopico = "Modulo da velocidade Linear"

    modulo = (data.x**2 + data.y**2 + data.z**2)**(1/2)#calculando o modulo e o-incluido na mensagem
    mensagemTopico = f"Modulo da velocidade Angular: {modulo} "
    rospy.loginfo(mensagemTopico)

    topico1.publish(modulo) #publicando no topico

def callback_vector3_angular(data):
    rospy.loginfo(rospy.get_caller_id() + "Mensagem recebida! -> '%f, %f, %f'", data.x, data.y, data.z)
    topico2 = rospy.Publisher('topico_modulo_VA', Float32, queue_size=10)
    
    modulo = (data.x**2 + data.y**2 + data.z**2)**(1/2)
    mensagemTopico = f"Modulo da velocidade Angular: {modulo} "
    rospy.loginfo(mensagemTopico)

    topico2.publish(modulo)

def listener():

    rospy.init_node('listener', anonymous=True)
    #inicializando o nó Listener
    rospy.Subscriber("topico_Status", String, callback_status)
    rospy.Subscriber("topico_Componentes_Velocidade_Linear", Vector3, callback_vector3_linear)
    rospy.Subscriber("topico_Componentes_Velocidade_Angular", Vector3, callback_vector3_angular)

    # rospy.Subscriber("topico_Componentes_Velocidade", Vector3, callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

   

if __name__ == '__main__':
    listener()