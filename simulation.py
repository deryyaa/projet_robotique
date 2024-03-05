from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.controleur.strategie import *
import math
import time
import threading
from tkinter import *

FPS=500

#Création de robot
robot = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde

# Création du monde
monde = Monde(500, 500,robot)




#Paramétrage graphique
fenetre = Tk()
fenetre.title("Robot dans le monde")
cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
cnv.pack()
graph=Graphique(monde,cnv)


lock=threading.Lock()


def update():
    while True:
        monde.update()
        graph.update()
        graph.dessineTrait()
        time.sleep(1./FPS)
        fenetre.update()


def runAvancer(FPS):
    graph.dessineObstacle()
    strategie=AvancerToutDroit(50,robot)
    threading.Thread(target=update).start()
    strategie.start()
    while True:
        strategie.step()
        if(strategie.stop() or robot.crash):
            break
        time.sleep(1./FPS)

def runTourner(FPS):
    graph.dessineObstacle()
    strategie=Tourner(math.pi,robot)
    threading.Thread(target=update).start()
    strategie.start()
    while True:
        strategie.step()
        if(strategie.stop() or robot.crash):
            break
        time.sleep(1./FPS)

def runTracerCarre(FPS):
    graph.dessineObstacle()
    strategie=TracerCarre(20,robot)
    threading.Thread(target=update).start()
    strategie.start()
    while True:
        strategie.step()
        if(strategie.stop() or robot.crash):
            break
        time.sleep(1./FPS)

#threading.Thread(target=runAvancer, args=(100,)).start()
#threading.Thread(target=runTourner, args=(100,)).start()
#threading.Thread(target=runTracerCarre, args=(100,)).start()

fenetre.mainloop()