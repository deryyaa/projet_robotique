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
fenetre = Tk()
fenetre.title("Robot dans le monde")
cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
cnv.pack()
graph=Graphique(monde,cnv,fenetre)
graph.dessineObstacle()

def update():
    while True:
        monde.update()
        graph.update()
        time.sleep(1./FPS)


def run(strat):
    threading.Thread(target=update).start()
    strat.start()
    while True:
        strat.step()
        if(strat.stop() or robot.crash):
            print(robot.capteur_distance(monde))
            robot.setVitesse(0,0)
            break
        time.sleep(1./FPS)

#threading.Thread(target=run, args=(TracerCarre(20,robot),)).start()
threading.Thread(target=run, args=(AvancerToutDroit(40,robot),)).start()
#threading.Thread(target=run, args=(Tourner(-math.pi/2,robot),)).start()

fenetre.mainloop()