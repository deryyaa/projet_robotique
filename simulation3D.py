from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.controleur.strategie import *
import math
import time
import threading
from tkinter import *
from src.graphique.graphique3D import Graphique3D


FPS = 100

# Création de robot
robot = Robot.creation_robot()

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde = monde
monde.place_obstacle()

# Création de l'instance Graphique3D
root = Tk()
graph = Graphique3D(monde, root)

# Paramétrage graphique
def update():
    graph.draw_obstacle()
    while True:
        monde.update()
        graph.update()
        time.sleep(1. / FPS)

def run(strat):
    condition = True
    threading.Thread(target=update).start()
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

root.mainloop()
