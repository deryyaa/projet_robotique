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
robot = Robot.creation_robot()

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde = monde
monde.place_obstacle()

# Création de l'instance Graphique3D
game = MyRobot(monde)

game.afficheRobot()

game.afficheObstacle()

game.afficheEnvironnement()

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

# Lancement de la stratégie
threading.Thread(target=run, args=(TracerCarre(50, robot),)).start()

game.taskMgr.add(update, "updateTask")
game.run()
