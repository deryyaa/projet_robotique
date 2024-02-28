import time
import math
from threading import Thread
class Controleur(Thread):
    def __init__(self,robot,FPS=100):
        self.robot = robot
        self.FPS=FPS

    class AvancerToutDroit():
        def __init__(self, distance,robot,FPS=100):
            self.distance = distance
            self.robot=robot
            self.FPS=FPS
                        
        def start(self):
            self.parcouru = 0

        def step(self):
            self.robot.vg = 10
            self.robot.vd = 10
            self.parcouru += abs(self.robot.vg*(1./self.FPS))
            if self.stop():
                self.robot.vg=0
                self.robot.vd=0
                return

        def stop(self):
            return self.parcouru>self.distance

  
    class Tourner:
        def __init__(self, angle, robot, FPS = 100):
            """
            Fait tourner le robot sur lui même avec un angle.

            angle: angle de rotation (en radians).
            robot: robot à faire tourner.
            FPS: taux de rafraîchissement en FPS (par défaut: 100).
            """
            # Initialisation des attributs avec les valeurs fournies
            self.robot.x = robot.x
            self.robot.y = robot.y
            self.angle = angle
            self.FPS=FPS
            
        def start(self):
            """Commence la rotation du robot en tournant avec un angle"""
            self.angletourner=1 #l'angle tourne de 1 à chaque step
        
        def step(self):
            """
            Fais une étape de rotation.
            """
            #calcul les nouvelles coordonnées du robot après une rotation
            self.robot.x=self.robot.x*math.cos(self.angletourner)-self.robot.y*math.sin(self.angletourner)
            self.robot.y=self.robot.x*math.cos(self.angletourner)-self.robot.y*math.sin(self.angletourner)
            
            self.angleparcouru+=self.angletourner  # met à jour de l'angle parcouru

        def stop(self):
            """
            Arrête de faire la rotation lorsque l'angle parcouru dépasse l'angle à tourner.
            """
            self.angle<self.angleparcouru

    class TracerCarre:
        def __init__(self, robot, distance, FPS = 100):
            self.robot = robot
            self.distance = distance
            self.FPS=FPS

        def start(self):
            self.parcouru = 0
            
        def step(self):
            if self.stop(): return
            Controleur.AvancerToutDroit.step()
            Controleur.Tourner.step()
            
