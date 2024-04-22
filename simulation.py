from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.controleur.strategie import *
import math
import time
import threading
from tkinter import *

FPS=100

#Création de robot
robot = Robot.creation_robot() 

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
        monde.update()
        time.sleep(1./FPS)



def run(strat,graphique):
    condition=True
    if(graphique):
        threading.Thread(target=update).start()
    else:
        threading.Thread(target=update_sans_graphique).start()
    strat.start()
    while condition:
        debut=time.time()
        strat.step()
        if(strat.stop() or robot.crash):
            print(robot.capteur_distance())
            robot.setVitesse(0,0)
            condition=False
        time.sleep(time.time()-debut)

threading.Thread(target=run, args=(TracerCarre(50,robot),True,)).start()
#threading.Thread(target=run, args=(AvancerToutDroit(40,robot),True,)).start()
#threading.Thread(target=run, args=(Tourner(-math.pi/2,robot),True,)).start()

try:
    fenetre.mainloop()
except NameError:
    pass