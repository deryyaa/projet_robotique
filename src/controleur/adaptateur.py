from src.controleur.robotReel import Robot2IN013_Mockup
import math
from src.univers.monde import Monde
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
        self.last_time=time.time()
        self.last_motor_pos=robot.get_motor_position()

    def move(self,dt):  #update, mise a jours des stats

        current_time = time.time()  # Obtient le temps actuel
        dt = current_time - self.last_time  # Calcule la différence de temps
        self.last_time = current_time  # Met à jour le temps de la dernière mise à jour

        #print(self.robot.get_motor_position(),type(self.robot.get_motor_position()))
        rg,rd=self.robot.get_motor_position()
        drg,drd=((rg,rd)[0]-self.last_motor_pos[0],(rg,rd)[1]-self.last_motor_pos[1])
        self.last_motor_pos=self.robot.get_motor_position()
        
        old_x=self.x
        old_y=self.y #vitess roue droite et droite
        distanceG=drg*self.robot.WHEEL_DIAMETER/2 #distance parcourue par la roue gauche
        distanceD=drd*self.robot.WHEEL_DIAMETER/2 #distance parcourue par la roue droite
        self.x += ((distanceG*dt+distanceD*dt)/2.0) * math.cos(self.dir)
        self.y += ((distanceG*dt+distanceD*dt)/2.0) * math.sin(self.dir)
        if(distanceG!=distanceD):
            if(abs(distanceG)>abs(distanceD)):
                self.dir-=distanceG*dt/(-self.d*distanceG*dt/(distanceD*dt-distanceG*dt))
            else:
                self.dir+=distanceD*dt/(-self.d*distanceD*dt/(distanceG*dt-distanceD*dt))
        self.distanceParcouru+=math.sqrt((self.x-old_x)**2+(self.y-old_y)**2)
        self.angle_parcourue=math.atan2(old_y-self.y,old_x-self.x) #angle entre deux points
        

        
    def setVitesse(self, vg,vd):
        self._vg=vg
        self._vd=vd
        self.robot.set_motor_dps(self.robot.MOTOR_LETF,vg)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vd)

    def getPosition(self):
        return (self.x,self.y)
    
    def getDistanceParcouru(self):
        return self.distanceParcouru
    
    def capteur_distance(self,monde):
        return self.robot.get_distance()