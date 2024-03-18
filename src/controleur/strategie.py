import time
import math
from threading import Thread


class AvancerToutDroit:
    def __init__(self, distance,robot, monde, FPS=100):
        self.distance = distance
        self.robot=robot
        self.monde=monde
        self.FPS=FPS
                    
    def start(self):
        self.robot.distanceParcouru=0

    def step(self):
        self.robot.setVitesse(10,10)
        if self.stop() or self.robot.crash:
            self.robot.setVitesse(0,0)
            self.distance=0

    def stop(self):
        return ((self.robot.distanceParcouru>self.distance) or (self.robot.capteur_distance(self.monde)<5))


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
            self.robot.setVitesse(-10,10)
        else:
            self.robot.setVitesse(10,-10)
        if self.stop() or self.robot.crash:
            self.robot.setVitesse(0,0)
        
    def stop(self):
        """
        Arrête de faire la rotation lorsque l'angle parcouru dépasse l'angle à tourner.
        """
        if self.angle<0:
            return self.robot.dir<self.angleArrive
        else:
            return self.robot.dir>self.angleArrive

class TracerCarre:
    def __init__(self, cote, robot, monde, FPS=100):
        self.robot = robot
        self.cote = cote
        self.FPS = FPS
        self.listeStrat = ListeStrat([AvancerToutDroit(cote, robot, monde), Tourner(math.pi/2, robot)])
        self.traceCote = 0

    def start(self):
        self.listeStrat.update()
        
    def step(self):

        if self.stop():
            self.robot.setVitesse(0,0)
            return

        self.listeStrat.liste[self.listeStrat.indice].step()
        
        if self.listeStrat.liste[self.listeStrat.indice].stop():
            self.listeStrat.update()
        
    def stop(self):
        return self.traceCote == 4


class ListeStrat:

    def __init__(self, liste):
        self.liste = liste
        self.indice = 0

    def update(self):
        self.liste[self.indice].step()
        if self.liste[self.indice].stop():
            self.indice += 1
			
    def stop(self):
        if self.indice >= len(self.liste):
            self.indice = 0
            return True
        return False
