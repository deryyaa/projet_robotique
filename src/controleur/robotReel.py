import time
import math
from io import BytesIO
import threading
from collections import deque

class Robot2IN013:
    """ 
    Classe d'encapsulation du robot et des senseurs.
    Constantes disponibles : 
    LED (controle des LEDs) :  LED_LEFT_EYE, LED_RIGHT_EYE, LED_LEFT_BLINKER, LED_RIGHT_BLINKER, LED_WIFI
    MOTEURS (gauche et droit) : MOTOR_LEFT, MOTOR_RIGHT
    et les constantes ci-dessous qui definissent les elements physiques du robot

    """

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    
    def __init__(self):
        """ 
            Initialise le robot
            :resolution: resolution de la camera
            :servoPort: port du servo (SERVO1 ou SERVO2)
            :motionPort: port pour l'accelerometre (AD1 ou AD2)
        """
  

    def stop(self):
        print("Arrete le robot")

    def get_image(self):
        pass

    def get_images(self):
        pass
  
    def set_motor_dps(self, port, dps):
        print("Fixe la vitesse d'un motor")

    def setVitesse(self, vg,vd):
        print("fixe vitesse des deux roues")


    def get_motor_position(self):
        print("lecture etats des moteurs en degre")
        return 1,1
    
    def getPosition():
        pass 
   
    def offset_motor_encoder(self, port, offset):
        print("Fixe l'offset des moteurs ")

    def get_distance(self):
        print("retourne distance")

    def servo_rotate(self,position):
        print("Tourne le servo a l'angle en para")

    def start_recording(self):
        pass

    def _stop_recording(self):
        pass
        
    def _start_recording(self):
        pass

    def __getattr__(self,attr):
        pass