import time
import math
from threading import Thread

class AvancerToutDroit():
    def __init__(self, distance,robot,FPS=100):
        self.distance = distance
        self.robot=robot
        self.FPS=FPS
                    
    def start(self):
        self.robot.distanceParcouru=0

    def step(self):
        self.robot.vg = 10
        self.robot.vd = 10
        if self.stop() or self.robot.crash:
            print("stop")
            self.robot.vg=0
            self.robot.vd=0
            exit

    def stop(self):
        return self.robot.distanceParcouru>self.distance


class Tourner:
    def __init__(self, angle, robot, FPS = 100):
        """
        Fait tourner le robot sur lui même avec un angle.
        angle: angle de rotation (en radians).
        robot: robot à faire tourner.
        FPS: taux de rafraîchissement en FPS (par défaut: 100).
        """
        # Initialisation des attributs avec les valeurs fournies
        self.robot=robot
        self.angle = angle
        self.FPS=FPS
        
    def start(self):
        """Commence la rotation du robot en tournant avec un angle"""
        self.angleArrive=self.robot.dir+self.angle
    
    def step(self):
        """
        Fais une étape de rotation.
        """
        if(self.angle>0):
            self.robot.vg=-10
            self.robot.vd=10
        else:
            self.robot.vg=10
            self.robot.vd=-10
        if self.stop() or self.robot.crash:
            self.robot.vg=0
            self.robot.vd=0
            return
        
    def stop(self):
        """
        Arrête de faire la rotation lorsque l'angle parcouru dépasse l'angle à tourner.
        """
        if self.angle<0:
            return self.robot.dir<self.angleArrive
        else:
            return self.robot.dir>self.angleArrive

class TracerCarre:
    def __init__(self,cote, robot, FPS = 100):
        self.robot = robot
        self.cote = cote
        self.FPS=FPS

    def start(self):
        self.traceCote = 0
        self.avancer=AvancerToutDroit(self.cote,self.robot)
        self.tourner=Tourner(math.pi/2,self.robot)
        self.strat=[self.avancer,self.tourner]
        self.strat[0].start()
        self.i=0
        self.tours=0
        
    def step(self):
        if self.strat[self.i].stop():
            if self.i==1:
                self.i=0
                self.tours=0
            else:
                self.i=1
                self.tours=0
                self.traceCote+=1
        if self.tours==0:
            self.strat[self.i].start()
        self.strat[self.i].step()
        self.tours+=1
        if self.stop():
            self.robot.vg=0
            self.robot.vd=0
            return
            
            
        
    def stop(self):
        return self.traceCote==4

