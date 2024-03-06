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
robot = Robot(300, 460, 20, 15 , 10 , math.pi/2)  # Position du robot dans le monde

# Création du monde
monde = Monde(500, 500, robot)
monde.place_obstacle()



#Paramétrage graphique
fenetre = Tk()
fenetre.title("Robot dans le monde")
cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
cnv.pack()
graph=Graphique(monde,cnv,fenetre)

def update():
    while True:
        monde.update()
        graph.update()
        robot.capteur_distance(monde)
        time.sleep(1./FPS)


def run(strat,FPS):
    graph.dessineObstacle()
    threading.Thread(target=update).start()
    strat.start()
    while True:
        strat.step()
        if(strat.stop() or robot.crash):
            break
        time.sleep(1./FPS)

#threading.Thread(target=run, args=(TracerCarre(50,robot),100,)).start()
threading.Thread(target=run, args=(AvancerToutDroit(50,robot),100,)).start()
#threading.Thread(target=run, args=(Tourner(50,robot),100,)).start()

fenetre.mainloop()