from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.controleur.strategie import *
import math
import time
import threading
from tkinter import *
from src.controleur.robotReel import Robot2IN013_Mockup
from src.controleur.adaptateur import Robot2I013Adaptateur

FPS=100

#Création de robot
robot = Robot.creation_robot() 

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde=monde
monde.place_obstacle()


robotMockup=Robot2IN013_Mockup()
robotReel= Robot2I013Adaptateur(robotMockup,300,250,20,20)

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
    if(graphique):
        threading.Thread(target=update).start()
    else:
        threading.Thread(target=update_sans_graphique).start()
    strat.start()
    while True:
        strat.step()
        if(strat.stop() or robot.crash):
            print(robot.capteur_distance())
            robot.setVitesse(0,0)
            break
        time.sleep(1./FPS)

threading.Thread(target=run, args=(TracerCarre(50,robot),True,)).start()
#threading.Thread(target=run, args=(AvancerToutDroit(40,robot),True,)).start()
#threading.Thread(target=run, args=(Tourner(-math.pi/2,robot),True,)).start()
        

#threading.Thread(target=run, args=(TracerCarre(50,robotReel),False,)).start()
#threading.Thread(target=run, args=(AvancerToutDroit(40,robot),False,)).start()
#threading.Thread(target=run, args=(Tourner(-math.pi/2,robot),False,)).start()

fenetre.mainloop()

