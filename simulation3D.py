from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.controleur.strategie import *
import math
import time
import threading
from direct.showbase.ShowBase import ShowBase
from src.graphique.graphique3D import MyRobot
import sys
import os

FPS = 100 # nombre d'image par seconde

# Création du robot aux coordonnées x,y,z
robot = Robot.creation_robot(252, 300, 0)


monde = Monde.creation_monde(robot) # Création et attribution du robot au monde
robot.monde = monde # Attribue au robot le monde
monde.place_obstacle() # Place les obstacles dans le monde

# Initialiser les differentes stratégie 
tracer_carre = TracerCarre(50, robot) # Tracer un carré de perimetre 4*50
avancer = AvancerToutDroit(50, robot) # Avancer tout droit avec un pas de 50m
avancer_infini = Avancer(robot) # Avancer sans limite de pas jusqu'à croiser un obstacle
immobile = None # Ne pas bouger 


# Création de l'instance Graphique3D avec strategie en paramètre
#game = MyRobot(monde, tracer_carre)
#game = MyRobot(monde, avancer)
#game = MyRobot(monde, immobile)
game = MyRobot(monde, avancer_infini) 

# Paramétrage graphique
def update(task):
    monde.update() # Cherche les collisions avec les obstacles, update la position du robot dans le monde
    game.update(task) # Update l'affichage 3D et le deplacement du robot dans l(interface 3D pour la simulation en cours
    return task.cont # Indique que la tâche doit continuer à être appelée chaque frame

def run(strat):
    condition = True
    strat.start() # Démarre la stratégie
    while condition:
        strat.step() # Exécute une étape de la stratégie
        if strat.stop() or robot.crash:  # Vérifie si la stratégie doit s'arrêter ou si le robot a crashé
            print("distance obstacle : ",robot.capteur_distance()) # Affiche la distance entre le robot et l'obstacle captée par le capteur de distance
            robot.setVitesse(0, 0) # Arrete le robot en conséquence
            condition = False # Fin de la boucle, on arrete la simulation
        time.sleep(1. / FPS) # Ralentit le déroulement de la boucle pour maintenir un taux de rafraîchissement constant

# Lancement de la stratégie dans un thread séparé
#threading.Thread(target=run, args=(avancer_infini,)).start()
#threading.Thread(target=run, args=(avancer,)).start()
threading.Thread(target=run, args=(tracer_carre,)).start()
#threading.Thread(target=run, args=(immobile,)).start()

game.taskMgr.add(update, "updateTask") # Specifie les tâches (l'update) à executer à chaque frame dans la simulation
game.run() # Demarre la simulation de la classe MyRobot
