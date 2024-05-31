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

FPS = 100

# Création de robot
robot = Robot.creation_robot(222, 220, 0)

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde = monde
monde.place_obstacle()

# Initialiser la stratégie TracerCarre
tracer_carre = TracerCarre(500, robot)

# Création de l'instance Graphique3D
game = MyRobot(monde, tracer_carre)

# Paramétrage graphique
def update(task):
    monde.update()
    game.update(task)
    return task.cont

def run(strat):
    condition = True
    strat.start()
    while condition:
        strat.step()
        if strat.stop() or robot.crash:
            print(robot.capteur_distance())
            robot.setVitesse(0, 0)
            condition = False
        time.sleep(1. / FPS)

# Lancement de la stratégie dans un thread séparé
threading.Thread(target=run, args=(tracer_carre,)).start()

game.taskMgr.add(update, "updateTask")
game.run()

game.taskMgr.add(update, "updateTask")
game.run()