from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.controleur.strategie import *
from src.controleur.adaptateur import Robot2I013Adaptateur
from direct.showbase.ShowBase import ShowBase
from src.graphique.graphique3D import MyRobot
import sys
import os
import math
import time
import threading
from tkinter import *

try:
    from robot2IN013 import Robot2IN013 as Robot
    robot=Robot2I013Adaptateur(Robot(),300,250,20,20)
except ImportError:
    from src.controleur.robotReel import Robot2IN013_Mockup
    robot = Robot2I013Adaptateur(Robot2IN013_Mockup(),300,250,20,20)

FPS = 100 # nombre d'image par seconde
GRAPH = 1 # 0-> sans graph // 1-> graph 2D // 2-> graph 3D

# Création du robot aux coordonnées x,y,z
robot = Robot.creation_robot(250,250,0) 

# Création du monde
monde = Monde.creation_monde(robot) # Création et attribution du robot au monde
robot.monde=monde # Attribue au robot le monde
monde.place_obstacle() # Place les obstacles dans le monde

# Initialiser les differentes stratégie 
tracer_carre = TracerCarre(50, robot) # Tracer un carré de perimetre 4*50
avancer = AvancerToutDroit(50, robot) # Avancer tout droit avec un pas de 50m
avancer_infini = Avancer(robot) # Avancer sans limite de pas jusqu'à croiser un obstacle

def update():
    
    # Parametrage graphique
    fenetre = Tk()
    fenetre.title("Robot dans le monde")
    cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
    cnv.pack()
    graph=Graphique(monde,cnv,fenetre)
    graph.dessineObstacle()
    
    while True:
        # Boucle d'actualisation du programme
        monde.update()
        graph.update()
        time.sleep(1./FPS)

def update3D(task):
    monde.update() # Cherche les collisions avec les obstacles, update la position du robot dans le monde
    game.update3D(task) # Update l'affichage 3D et le deplacement du robot dans l(interface 3D pour la simulation en cours
    return task.cont # Indique que la tâche doit continuer à être appelée chaque frame


def update_sans_graphique():
    while True:
        try:
            monde.update()
        except NameError:
            robot.update()
        time.sleep(1./FPS)

def creation3D():
    # Création de l'instance Graphique3D
    pass
    
def run(strat,graphique):
    condition=True
    if(graphique==0):
        threading.Thread(target=update_sans_graphique).start()
    elif(graphique==1):
        threading.Thread(target=update).start()
        time.sleep(1.5)
    elif(graphique==2):
        pass
    strat.start()
    while condition:
        debut=time.time()
        strat.step()
        if GRAPH==0:
            print(robot.x,robot.y,robot.z)
        if(strat.stop() or robot.crash):
            robot.setVitesse(0,0)
            robot.stopRec()
            condition=False
        time.sleep(time.time()-debut)

threading.Thread(target=run, args= (TracerCarre(50,robot),GRAPH)).start()
#run(AvancerToutDroit(50,robot),True)
#run(Tourner(math.pi/2,robot),True)

try:
    if GRAPH==2:
        game = MyRobot(monde,tracer_carre)
        game.taskMgr.add(update3D, "updateTask") # Specifie les tâches (l'update) à executer à chaque frame dans la simulation
        game.run() # Demarre la simulation de la classe MyRobot
except NameError:
    pass

try:
    fenetre.mainloop()
except NameError:
    pass