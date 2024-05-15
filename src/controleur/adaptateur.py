from src.controleur.robotReel import Robot2IN013_Mockup
import math
import time


class Robot2I013Adaptateur():
    def __init__(self,robot,x,y,longueur,largeur,monde=None):
        self.monde=monde
        self.robot=robot
        self.x=x
        self.y=y
        self._vg=1 #on ne touche pas aux valeur vg et vd
        self._vd=1
        self.dir=0
        self.distanceParcouru=0
        self.largeur = largeur 
        self.longueur = longueur 
        self.crash=False
        self.taille_roue = 8
        self.angle_parcourue=0
        self.d=largeur
        self.last_motor_pos=robot.get_motor_position()

    def update(self):  #update, mise a jours des stats
        #print(self.robot.get_motor_position(),type(self.robot.get_motor_position()))
        rg,rd=self.robot.get_motor_position()
        drg,drd=((rg,rd)[0]-self.last_motor_pos[0],(rg,rd)[1]-self.last_motor_pos[1])
        self.last_motor_pos=self.robot.get_motor_position()
        distanceG=math.radians(drg)*self.robot.WHEEL_DIAMETER/2.0 #distance parcourue par la roue gauche
        distanceD=math.radians(drd)*self.robot.WHEEL_DIAMETER/2.0 #distance parcourue par la roue droite
        if(distanceG!=distanceD):
            if(abs(distanceG)>abs(distanceD)):
                self.angle_parcourue-=distanceG/(float)(-self.robot.WHEEL_BASE_WIDTH*distanceG/(float)(distanceD-distanceG))
            else:
                self.angle_parcourue+=distanceD/(float)(-self.robot.WHEEL_BASE_WIDTH*distanceD/(float)(distanceG-distanceD))
        self.distanceParcouru+=(distanceG+distanceD)/2.0


    def getDistanceParcouru(self):
        return self.distanceParcouru

        
    def setVitesse(self, vg,vd):
        if vg==vd:
            self.robot.set_motor_dps(3,vg)
        else:
            self.robot.set_motor_dps(1,vg)
            self.robot.set_motor_dps(2,vd)

    
    def capteur_distance(self):
        return 1000