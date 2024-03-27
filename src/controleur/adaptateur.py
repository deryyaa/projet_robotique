from src.controleur.robotReel import Robot2IN013
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

    def move(self,dt):  #update, mise a jours des stats

        current_time = time.time()  # Obtient le temps actuel
        dt = current_time - self.last_time  # Calcule la différence de temps
        self.last_time = current_time  # Met à jour le temps de la dernière mise à jour

        print(self.robot.get_motor_position(),type(self.robot.get_motor_position()))
        rg,rd=self.robot.get_motor_position()
        old_x=self.x
        old_y=self.y #vitess roue droite et droite
        vg=rg*self.robot.WHEEL_DIAMETER/2
        vd=rd*self.robot.WHEEL_DIAMETER/2
        self.x += ((vg*dt+vd*dt)/2.0) * math.cos(self.dir)
        self.y += ((vg*dt+vd*dt)/2.0) * math.sin(self.dir)
        if(self._vg!=self._vd):
            if(abs(vg)>abs(vd)):
                self.dir-=vg*dt/(-self.d*vg*dt/(vd*dt-vg*dt))
            else:
                self.dir+=vd*dt/(-self.d*vd*dt/(vg*dt-vd*dt))
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
        distanceP_capteur = 0
        capteur_x = self.x+self.longueur
        capteur_y = self.y+self.largeur
        rg,rd=self.robot.get_motor_position()
        vg=rg*self.robot.WHEEL_DIAMETER/2
        vd=rd*self.robot.WHEEL_DIAMETER/2

        while not monde.detecter_collision(capteur_x, capteur_y): #tant qu'il n'a rien detecté, on fait avancer le capteur dans la direction de robot et on incremente sa distance parcourue
            distanceP_capteur+= 1
            if distanceP_capteur>50:
                return distanceP_capteur
            capteur_x += ((vg*0.01+vd*0.01)/2.0) * math.cos(self.dir)
            capteur_y += ((vg*0.01+vd*0.01)/2.0) * math.sin(self.dir)
            
        print(f"Position actuelle du robot : {[self.x, self.y]}, Distance jusqu'a l'obstacle : {distanceP_capteur}")
        return distanceP_capteur    
