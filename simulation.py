from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.controleur.strategie import *
from src.controleur.adaptateur import Robot2I013Adaptateur
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

FPS=100 # nombre d'image par seconde

#Création de robot
robot = Robot.creation_robot(250,250,0) 

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde=monde
monde.place_obstacle()

#Paramétrage graphique

def update():
    fenetre = Tk()
    fenetre.title("Robot dans le monde")
    cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
    cnv.pack()
    graph=Graphique(monde,cnv,fenetre)
    graph.dessineObstacle()
    while True:
        monde.update()
        graph.update()
        time.sleep(1./FPS)

def update_sans_graphique():
    while True:
        try:
            monde.update()
        except NameError:
            robot.update()
        time.sleep(1./FPS)



def run(strat,graphique):
    condition=True
    if(graphique):
        threading.Thread(target=update).start()
        time.sleep(1.5)
    else:
        threading.Thread(target=update_sans_graphique).start()
    strat.start()
    while condition:
        debut=time.time()
        strat.step()
        if(strat.stop() or robot.crash):
            robot.setVitesse(0,0)
            robot.stopRec()
            condition=False
        time.sleep(time.time()-debut)

run(TracerCarre(50,robot),True)
#run(AvancerToutDroit(50,robot),True)
#run(Tourner(math.pi/2,robot),True)

try:
    fenetre.mainloop()
except NameError:
    pass