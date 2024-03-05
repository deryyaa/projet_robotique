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
        print("step")
        if self.stop() or self.robot.crash:
            print("stop")
            self.robot.vg=0
            self.robot.vd=0
            return

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
        self.angleparcouru=0
    
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
        self.angleparcouru+=self.robot.vg*(1./self.FPS)/(self.robot.d/2)
        self.robot.update()
        if self.stop() or self.robot.crash:
            self.robot.vg=0
            self.robot.vd=0
            return
        
    def stop(self):
        """
        Arrête de faire la rotation lorsque l'angle parcouru dépasse l'angle à tourner.
        """
        return abs(self.angle)<abs(self.angleparcouru)

class TracerCarre:
    def __init__(self,cote, robot, FPS = 100):
        self.robot = robot
        self.cote = cote
        self.FPS=FPS

    def start(self):
        self.traceCote = 0
        
    def step(self):
        avancer=AvancerToutDroit(self.cote,self.robot)
        tourner=Tourner(math.pi/2,self.robot)
        strat=[avancer,tourner]
        i=0
        tours=0
        if strat[i].stop():
            if i==1:
                i=0
            else:
                i=1
        elif self.stop():
            self.robot.vg=0
            self.robot.vd=0
            return
        else:
            if tours==0:
                strat[i].start()
            strat[i].step()
            
            
        
    def stop(self):
        if (self.traceCote>4):
            return True

