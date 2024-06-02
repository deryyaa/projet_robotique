import time
import math
from threading import Thread
from src.controleur.adaptateur import Robot2I013Adaptateur
#from src.camera.camera import isBalise

VITESSE = 100

class AvancerToutDroit:
    def __init__(self, distance,robot):
        """
        Stratégie qui fait avancé le robot d'une distance (en mm)
        Args:
            distance (float): Distance a parcourir pour le robot (en mm)
            robot (Object): Robot que l'on contrôle
        """
        self.distance = distance
        self.robot=robot
                    
    def start(self):
        """
        Met les compteur de la distance parcourue a 0
        """
        self.robot.distanceParcouru=0.0
        self.robot.resetMotor(3,0)

    def step(self):
        """
        Donne la vitesse aux roues du robot pour allez tout droit, et ralenti lorsqu'on se rapproche de la distance a parcourir.
        """
        self.robot.setVitesse(VITESSE,VITESSE)
        if self.distance-self.robot.distanceParcouru<2:
            self.robot.setVitesse(VITESSE/50.0,VITESSE/50.0)  

    def stop(self):
        """
        Donne l'information s'il faut s'arreté, True si il faut s'arrêté et False si il faut continué
        """
        return ((self.robot.distanceParcouru>self.distance) or (self.robot.capteur_distance()<50))

class Avancer:
    def __init__(self,robot):
        """
        Stratégie qui fait avancé en continue jusqu'a trouvé un obstacle
        Args:
            robot (Object): Robot que l'on contrôle
        """
        self.robot=robot
                    
    def start(self):
        """
        Met les compteur de la distance parcourue a 0
        """
        self.robot.distanceParcouru=0.0
        self.robot.resetMotor(3,0)

    def step(self):
        """
        Donne la vitesse aux roues du robot pour allez tout droit
        """
        self.robot.setVitesse(VITESSE,VITESSE)

    def stop(self):
        """
        Donne l'information s'il faut s'arreté, True si il faut s'arrêté et False si il faut continué
        """
        return self.robot.capteur_distance()<50

class Tourner:
    def __init__(self, angle, robot):
        """
        Fait tourner le robot sur lui même avec un angle.
        angle (float): angle de rotation (en radians).
        robot (Object): robot à faire tourner.
        """
        # Initialisation des attributs avec les valeurs fournies
        self.robot=robot
        self.angle = angle
        
    def start(self):
        """
        Met les compteur d'angle parcourue a 0
        """
        self.robot.angle_parcourue=0
        self.robot.resetMotor(3,0)
    
    def step(self):
        """
        Donne la vitesse aux roues du robot pour tourné sur lui même, et ralenti lorsqu'on se rapproche de l'objectif
        """
        if(self.angle>0):
            if self.angle-self.robot.angle_parcourue<math.pi/16.0:
                self.robot.setVitesse(-VITESSE/100.0,VITESSE/100.0)
            else:
                self.robot.setVitesse(-VITESSE/2.0,VITESSE/2.0)
                 
        else:
            if self.angle-self.robot.angle_parcourue<-math.pi/16.0:
                self.robot.setVitesse(VITESSE/100.0,-VITESSE/100.0)
            else:
                self.robot.setVitesse(VITESSE/2.0,-VITESSE/2.0)
        
    def stop(self):
        """
        Donne l'information s'il faut s'arreté, True si il faut s'arrêté et False si il faut continué
        """
        if self.angle<0:
            return self.robot.angle_parcourue<self.angle
        else:
            return self.robot.angle_parcourue>self.angle


class TracerCarre:
    def __init__(self, cote, robot):
        """
        Stratégie qui fait faire un déplacement carré au robot
        Args:
            robot (Object): Robot que l'on contrôle
            cote (float): Largeur du carré en mm
            listeStrat (Object): Liste de stratégie pour faire un déplacement carré
        """
        self.robot = robot
        self.cote = cote
        self.listeStrat = ListeStrat([AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot),AvancerToutDroit(cote, robot), Tourner(math.pi/2, robot)],robot)

    def start(self):
        """
        Appel listeStrat.start
        """
        self.listeStrat.start()
        
    def step(self):
        """
        Appel listeStrat.step
        """
        self.listeStrat.step()
        
    def stop(self):
        """
        Appel listeStrat.stop
        """
        return self.listeStrat.stop()

class ListeStrat:

    def __init__(self, liste, robot):
        """
        Execute une liste de strategie a la suite
        Args:
            liste (List[Object]): La liste des strategie a execute
            robot (Object): Robot que l'on contrôle
            debut (int): donne l'information si c'est le debut ou non de la strategie (0 -> debut)
            indice (int): Position dans la liste
        """
        self.liste = liste
        self.indice = 0
        self.debut = 0
        self.robot=robot
    
    def start(self):
        """
        Met le fil d'execution au debut de la liste
        """
        self.indice = 0
        self.debut = 0

    def step(self):
        """
        Execute une strategie, et passe a la suivante s'il est terminé
        """
        if not self.stop():
            if self.debut==0:
                self.liste[self.indice].start()
            self.liste[self.indice].step()
            self.debut=1
            if self.liste[self.indice].stop():
                self.debut=0
                self.indice += 1
                time.sleep(0.1)

    def stop(self):
        """
        Donne l'information s'il faut s'arreté, True si il faut s'arrêté et False si il faut continué
        """
        return self.indice>=len(self.liste)

# Non-Fonctionnel
"""
class RepereBalise:
    
    def __init__(self,robot):
        self.robot=robot
        
    def start(self):
        self.robot.angle_parcourue=0
        self.robot.resetMotor(3,0)
        self.robot.rec()
    
    def step(self):
        if(isBalise(self.robot.getImage())):
            self.robot.stopRec()
            self.robot.setVitesse(VITESSE,VITESSE)
        else:
            self.robot.setVitesse(-VITESSE,VITESSE)
    
    def stop(self):
        return self.robot.angle_parcourue>=2*math.pi
"""
