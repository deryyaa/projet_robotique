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
        monde.update()
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
        print(robot.distanceParcouru,robot.angle_parcourue)
        strat.step()
        if(strat.stop() or robot.crash):
            print("distance obstacle : ",robot.capteur_distance()) # Affiche la distance entre le robot et l'obstacle captée par le capteur de distance
            robot.setVitesse(0,0)
            condition=False
        time.sleep(time.time()-debut)

run(TracerCarre(50,robot),True)
#run(AvancerToutDroit(1000,robot),True)
#run(Avancer(robot),True)
#run(Tourner(math.pi/2,robot),True)
#run(None,True)

try:
    fenetre.mainloop()
except NameError:
    pass