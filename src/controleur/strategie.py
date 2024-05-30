import time
import math
from threading import Thread
from src.controleur.adaptateur import Robot2I013Adaptateur

VITESSE = 50

class AvancerToutDroit:
    def __init__(self, distance,robot):
        self.distance = distance
        self.robot=robot
                    
    def start(self):
        self.robot.distanceParcouru=0
        self.robot.angle_parcourue=0

    def step(self):
        self.robot.setVitesse(VITESSE,VITESSE)
        if self.distance-self.robot.distanceParcouru<1:
            print("ralenti")
            self.robot.setVitesse(VITESSE/15.0,VITESSE/15.0)  

    def stop(self):
        return ((self.robot.distanceParcouru>self.distance) or (self.robot.capteur_distance()<50))

class Avancer:
    def __init__(self,robot):
        self.robot=robot
                    
    def start(self):
        self.robot.distanceParcouru=0

    def step(self):
        self.robot.setVitesse(VITESSE,VITESSE)

    def stop(self):
        return self.robot.capteur_distance()<50

class Tourner:
    def __init__(self, angle, robot):
        """
        Fait tourner le robot sur lui même avec un angle.
        angle: angle de rotation (en radians).
        robot: robot à faire tourner.
        FPS: taux de rafraîchissement en FPS (par défaut: 100).
        """
        # Initialisation des attributs avec les valeurs fournies
        self.robot=robot
        self.angle = angle
        
    def start(self):
        """Commence la rotation du robot en tournant avec un angle"""
        self.robot.angle_parcourue=0
        self.robot.distanceParcouru=0
    
    def step(self):
        """
        Fais une étape de rotation.
        """
        if(self.angle>0):
            if self.angle-self.robot.angle_parcourue<math.pi/64.0:
                print("ralenti")
                self.robot.setVitesse(-VITESSE/30.0,VITESSE/30.0)
            else:
                self.robot.setVitesse(-VITESSE/2.0,VITESSE/2.0)
                 
        else:
            if self.angle-self.robot.angle_parcourue<-math.pi/64.0:
                print("ralenti")
                self.robot.setVitesse(VITESSE/30.0,-VITESSE/30.0)
            else:
                self.robot.setVitesse(VITESSE/2.0,-VITESSE/2.0)
        
    def stop(self):
        """
        Arrête de faire la rotation lorsque l'angle parcouru dépasse l'angle à tourner.
        """
        if self.angle<0:
            return self.robot.angle_parcourue<self.angle
        else:
            return self.robot.angle_parcourue>self.angle

class TracerCarre:
    def __init__(self, cote, robot):
        self.robot = robot
        self.cote = cote
        self.listeStrat = ListeStrat([AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot)],self.robot)

    def start(self):
        self.listeStrat.start()
        
    def step(self):
        self.listeStrat.step()
        
    def stop(self):
        return self.listeStrat.stop()


class ListeStrat:

    def __init__(self, liste, robot):
        self.liste = liste
        self.indice = 0
        self.tours = 0
        self.robot=robot
    
    def start(self):
        self.indice = 0
        self.tours = 0

    def step(self):
        if not self.stop():
            if self.tours==0:
                self.liste[self.indice].start()
            self.liste[self.indice].step()
            self.tours=1
        if self.liste[self.indice].stop():
            self.tours=0
            self.indice += 1

    def stop(self):
        return self.indice>=len(self.liste)