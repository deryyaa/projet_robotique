from src.dexter.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
import math
import time
from src.univers.controleur import Controleur


# Création du monde
monde = Monde(500, 500)

# Création du robot dans le monde
robot = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde
#création de 2 obstacle 

controleur=Controleur()


def update(distance):
    controleur.avancer_tout_droit(distance)
        