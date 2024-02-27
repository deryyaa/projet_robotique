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
        monde.update(robot)
        graph.update()
        time.sleep(1./FPS)

def run(FPS):
    Thread(target=controleur.step).start()
    Thread(target=update).start()
    update()
    controleur.step()
    fenetre.mainloop()
run(100)