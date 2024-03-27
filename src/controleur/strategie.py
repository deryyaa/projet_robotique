import time
import math
from threading import Thread
from src.controleur.adaptateur import Robot2I013Adaptateur

VITESSE = 40

class AvancerToutDroit:
    def __init__(self, distance,robot):
        self.distance = distance
        self.robot=robot
        self.monde=robot.monde
                    
    def start(self):
        self.robot.distanceParcouru=0

    def step(self):
        self.robot.setVitesse(VITESSE,VITESSE)

    def stop(self):
        return ((self.robot.distanceParcouru>self.distance) or (self.robot.capteur_distance(self.monde)<20))

class Avancer:
    def __init__(self,robot):
        self.robot=robot
        self.monde=robot.monde
                    
    def start(self):
        self.robot.distanceParcouru=0

    def step(self):
        self.robot.setVitesse(VITESSE,VITESSE)

    def stop(self):
        return self.robot.capteur_distance(self.monde)<40

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
        self.angleArrive=self.robot.dir+self.angle
    
    def step(self):
        """
        Fais une étape de rotation.
        """
        if(self.angle>0):
            self.robot.setVitesse(-VITESSE,VITESSE)
        else:
            self.robot.setVitesse(VITESSE,-VITESSE)
        
    def stop(self):
        """
        Arrête de faire la rotation lorsque l'angle parcouru dépasse l'angle à tourner.
        """
        if self.angle<0:
            return self.robot.dir<self.angleArrive
        else:
            return self.robot.dir>self.angleArrive

class TracerCarre:
    def __init__(self, cote, robot):
        self.robot = robot
        self.cote = cote
        self.listeStrat = ListeStrat([AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot)])

    def start(self):
        self.listeStrat.update()
        
    def step(self):
        self.listeStrat.update()
        
    def stop(self):
        return self.listeStrat.stop()


class ListeStrat:

    def __init__(self, liste):
        self.liste = liste
        self.indice = 0
        self.tours = 0

    def update(self):
        if self.tours==0:
            self.liste[self.indice].start()
        self.liste[self.indice].step()
        self.tours+=1
        if self.liste[self.indice].stop():
            self.tours=0
            self.indice += 1
    
    def stop(self):
        return self.indice>=len(self.liste)
