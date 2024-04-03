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

    def update(self):  #update, mise a jours des stats

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
        self.x += ((distanceG+distanceD)/2.0) * math.cos(self.dir)
        self.y += ((distanceG+distanceD)/2.0) * math.sin(self.dir)
        if(distanceG!=distanceD):
            if(abs(distanceG)>abs(distanceD)):
                self.dir-=distanceG/(-self.d*distanceG/(distanceD-distanceG))
            else:
                self.dir+=distanceD/(-self.d*distanceD/(distanceG-distanceD))
        self.distanceParcouru+=math.sqrt((self.x-old_x)**2+(self.y-old_y)**2)
        self.angle_parcourue=math.atan2(old_y-self.y,old_x-self.x) #angle entre deux points

    def reset_distance(self):
        self.distanceParcouru=0
        
    def reset_angle_parcourue(self):
        self.angle_parcourue=0
        
    def getMonde(self):
        return self.monde
    
    def setMonde(self,monde):
        self.monde=monde

    def getDistanceParcouru(self):
        return self.distanceParcouru
    
    def setDistanceParcouru(self,dist):
        self.distanceParcouru = dist

    def getDistanceRoues(self):
        return self.d

    def setDistanceRoues(self,dist):
        self.d = dist
    
    def getVitesseMax(self):
        return self.vitesse_max
    
    def setVitesseMax(self,v):
        self.vitesse_max=v

    def getVitesseRoues(self):
        return self.vg,self.vd
    
    def setVitesse(self,vg,vd):
        self.vg=vg
        self.vd=vd

    def getNom(self):
        return self.nom
    
    def setNom(self,n):
        self.nom=n

    def getPosition(self):
        return (self.x,self.y)
    
    def setPosition(self,x,y):
        self.x=x
        self.y=y

    def getDir(self):
        return self.dir
    
    def setDir(self,d):
        self.d = d % (2*math.pi)

    def getLongLarg(self):
        return self.longueur,self.largeur
    
    def setLongLarg(self,long,larg):
        self.longueur = long
        self.largeur = larg
        
    def setVitesse(self, vg,vd):
        self._vg=vg
        self._vd=vd
        self.robot.set_motor_dps(self.robot.MOTOR_LETF,vg)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vd)

    
    def capteur_distance(self):
        return self.robot.get_distance()