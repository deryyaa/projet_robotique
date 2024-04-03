from src.univers.robot import Robot
from src.controleur.robotReel import Robot2IN013_Mockup
from src.controleur.adaptateur import Robot2I013Adaptateur
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.controleur.strategie import *
import math
import time
import threading
import random

FPS=100

#Création de robot
#robot = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde
robotreel=Robot2IN013_Mockup()
robot= Robot2I013Adaptateur(robotreel,300,250,20,20)

# Création du monde
monde = Monde(500, 500, robot)
robot.monde=monde

def update():
    while True:
        monde.update()
        time.sleep(1./FPS)

def run(strat):
    threading.Thread(target=update).start()
    strat.start()
    while True:
        strat.step()
        print(robot.distanceParcouru,robot.angle_parcourue)
        if(strat.stop() or robot.crash):
            print(robot.capteur_distance(monde))
            robot.setVitesse(0,0)
            break
        time.sleep(1./FPS)


#threading.Thread(target=runAvancer, args=(100,)).start()
#threading.Thread(target=runTourner, args=(100,)).start()

threading.Thread(target=run, args=(TracerCarre(20,robot),)).start()
#threading.Thread(target=runAvancer, args=(AvancerToutDroit(30,robot),)).start()
#threading.Thread(target=run, args=(Tourner(-math.pi/2,robot),)).start()

