from src.dexter.robot import Robot
from src.univers.monde import Monde
from src.univers.utilitaire import collision_rect

#import graphique
import time

FPS=150 # Declaration du nombre d'image par secondes
robot1 = Robot(300, 200, 50, 30 , 50) # Déclaration du robot

def step():
    """Fonction qui actualise tous d'un pas"""
    
    time.sleep(1./FPS)