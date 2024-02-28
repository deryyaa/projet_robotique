from src.dexter.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.univers.controleur import Controleur
import math
import time
from threading import Thread
from tkinter import *

FPS=100

# Création du monde
monde = Monde(500, 500)

# Création du robot dans le monde
robot = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde

monde.robot=robot

#Paramétrage graphique
fenetre = Tk()
fenetre.title("Robot dans le monde")
cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
cnv.pack()
graph=Graphique(monde,cnv)

controleur=Controleur(robot)

def update():
    while True:
        robot.update()
        monde.update(robot)
        graph.update()
        time.sleep(1./FPS)
        fenetre.update()


def run(FPS):
    graph.dessineObstacle()
    strategie=controleur.Tourner(math.pi,robot)
    Thread(target=update).start()
    strategie.start()
    while not strategie.stop():
        strategie.step()
        time.sleep(1./FPS)

Thread(target=run, args=(100,)).start()
fenetre.mainloop()