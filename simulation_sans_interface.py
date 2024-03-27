from src.univers.robot import Robot
from src.univers.robotReel import Robot2IN013
from src.univers.adaptateur import Robot2I013Adaptateur
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.controleur.strategie import *
import math
import time
import threading

FPS=100

#Création de robot
#robot = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde
robotreel=Robot2IN013()
robot= Robot2I013Adaptateur(robotreel,300,250,20,20)

# Création du monde
monde = Monde(500, 500,robot)
robot.monde=monde
lock=threading.Lock()

def update():
    while True:
        monde.update()
        time.sleep(1./FPS)
        

def runAvancer(FPS):
    strategie=AvancerToutDroit(100,robot)
    threading.Thread(target=update).start()
    strategie.start()
    while not strategie.stop():
        strategie.step()
        break
        time.sleep(1./FPS)

def runTourner(FPS):

    strategie=Tourner(math.pi,robot)
    threading.Thread(target=update).start()
    strategie.start()
    while not strategie.stop():
        strategie.step()
        time.sleep(1./FPS)

#threading.Thread(target=runAvancer, args=(100,)).start()
#threading.Thread(target=runTourner, args=(100,)).start()


#threading.Thread(target=run, args=(TracerCarre(20,robot),)).start()
threading.Thread(target=runAvancer, args=(AvancerToutDroit(30,robot),)).start()
#threading.Thread(target=run, args=(Tourner(-math.pi/2,robot),)).start()

