#!/usr/bin/env python3

import rospy
import random

from std_msgs.msg import String
# importando mensagens do tipo string
from geometry_msgs.msg import Vector3
# importando mensagens to tipo array de float 32

def talker():
    
    topico1 = rospy.Publisher('topico_Status', String, queue_size=1)
    topico2 = rospy.Publisher('topico_Componentes_Velocidade_Linear', Vector3, queue_size=1)
    topico3 = rospy.Publisher('topico_Componentes_Velocidade_Angular', Vector3, queue_size=1)

    # declarando os topicos topico_Componentes_Velocidades linear e angular
    
    rospy.init_node('talker', anonymous=True)
    # inicializando um nó
    
    rate = rospy.Rate(2) 
    # Numero de mensagens por segundo (Hz)
    
    vetorVelocidadesLinear = Vector3()
    #ciando um vetor de 3 cordenadas que vai guardar as velociades
    
    vetorVelocidadesAngular = Vector3()


    while not rospy.is_shutdown():
        # enquanto o nó estiver rodando, executar:
        
        mensagem_str = "Enviando mensagem" # criando uma nova mensagem

        vetorVelocidadesLinear.x = random.uniform(0 , 10.0)# mensagem array de ponto flutuante com componentes aleatorias
        vetorVelocidadesLinear.y = random.uniform(0 , 10.0)
        vetorVelocidadesLinear.z = random.uniform(0 , 10.0)

        vetorVelocidadesAngular.x = random.uniform(0 , 10.0)# mensagem array de ponto flutuante com componentes aleatorias
        vetorVelocidadesAngular.y = random.uniform(0 , 10.0)
        vetorVelocidadesAngular.z = random.uniform(0 , 10.0)
        
        rospy.loginfo(mensagem_str) # publicando no terminal
        rospy.loginfo(vetorVelocidadesLinear)
        rospy.loginfo(vetorVelocidadesAngular)

        
        topico1.publish(mensagem_str) # publicando no topico topico_Status a mensagem String
        topico2.publish(vetorVelocidadesLinear) # publicando no topico 
        topico3.publish(vetorVelocidadesAngular)
        
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
