import time
import math
import random
from io import BytesIO
import threading
from collections import deque

class Robot2IN013_Mockup:
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

    MOTOR_LETF  = 1
    MOTOR_RIGHT = 2
    
    def __init__(self,angle_gauche=0,angle_droit=0,dps_gauche=0,dps_droit=0):
        """ 
            Initialise le robot
            :resolution: resolution de la camera
            :servoPort: port du servo (SERVO1 ou SERVO2)
            :motionPort: port pour l'accelerometre (AD1 ou AD2)
        """
        self.angle_gauche=0
        self.angle_droit=0
        self.dps_gauche=0
        self.dps_droit=0

    def stop(self):
        print("Arrete le robot")

    def get_image(self):
        pass

    def get_images(self):
        pass
  
    def set_motor_dps(self, port, dps):
        print(f"Fixe la vitesse d'un motor port = {port}, dps = {dps}")
        if (port==1):
            self.dps_gauche=dps
        if (port==2):
            self.dps_droit=dps
        if (port==3):
            self.dps_gauche=dps
            self.dps_droit=dps


    def setVitesse(self, vg,vd):
        print("fixe vitesse des deux roues")

    def get_motor_position(self):
        #print("lecture etats des moteurs en degre")
        self.angle_droit+=self.dps_droit
        self.angle_gauche+=self.dps_gauche
        return (self.angle_gauche,self.angle_droit)

    def getPosition():
        pass 
   
    def offset_motor_encoder(self, port, offset):
        print("Fixe l'offset des moteurs ")

    def get_distance(self):
        print("retourne distance")
        return 1

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