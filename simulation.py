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

# Tentative d'import des classes spécifiques au robot réel
try:
    from robot2IN013 import Robot2IN013 as Robot
    robot = Robot2I013Adaptateur(Robot(), 300, 250, 20, 20)
except ImportError:
    # Utilisation d'un mockup du robot réel si l'import échoue
    from src.controleur.robotReel import Robot2IN013_Mockup
    robot = Robot2I013Adaptateur(Robot2IN013_Mockup(), 300, 250, 20, 20)

FPS = 100 # nombre d'image par seconde
GRAPH = 2 # 0-> sans graph // 1-> graph 2D // 2-> graph 3D

# Création du robot aux coordonnées x,y,z
robot = Robot.creation_robot(252, 300,0) 

# Création du monde
monde = Monde.creation_monde(robot) # Création et attribution du robot au monde
robot.monde=monde # Attribue au robot le monde
monde.place_obstacle() # Place les obstacles dans le monde

# Initialiser les differentes stratégie 
tracer_carre = TracerCarre(50, robot) # Tracer un carré de perimetre 4*50
avancer = AvancerToutDroit(50, robot) # Avancer tout droit avec un pas de 50m
avancer_infini = Avancer(robot) # Avancer sans limite de pas jusqu'à croiser un obstacle

def update():
    """ Met à jour l'interface graphique en 2D avec les informations du monde et des objets. """
    # Paramétrage de l'interface graphique
    fenetre = Tk()  # Crée une nouvelle fenêtre Tkinter
    fenetre.title("Robot dans le monde")  # Définit le titre de la fenêtre
    cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")  # Crée un canevas avec les dimensions du monde et un fond de couleur ivoire
    cnv.pack()  # Place le canevas dans la fenêtre
    graph = Graphique(monde, cnv, fenetre)  # Crée un objet Graphique pour représenter le monde dans le canevas
    graph.dessineObstacle()  # Dessine les obstacles dans le canevas
    
    while True:
        # Boucle d'actualisation du programme
        monde.update()  # Met à jour les objets dans le monde (positions, collisions, etc.)
        graph.update()  # Met à jour l'affichage graphique dans le canevas
        time.sleep(1. / FPS)  # Attend un certain temps pour respecter le taux de rafraîchissement de l'écran

def update3D(task):
    """ Met à jour l'interface graphique en 3D avec les informations du monde et des objets. """
    monde.update() # Cherche les collisions avec les obstacles, update la position du robot dans le monde
    game.update3D(task) # Update l'affichage 3D et le deplacement du robot dans l(interface 3D pour la simulation en cours
    return task.cont # Indique que la tâche doit continuer à être appelée chaque frame


def update_sans_graphique():
    """ Met à jour le monde sans interface graphique."""
    while True:
        try:
            monde.update()  # Met à jour les objets dans le monde (positions, collisions, etc.)
        except NameError:
            robot.update()  # Si le monde n'est pas défini, met à jour le robot uniquement
        time.sleep(1. / FPS)  # Attend un certain temps pour respecter le taux de rafraîchissement du programme
    
def run(strat, graphique):
    """ 
    Lance l'exécution de la stratégie donnée avec ou sans interface graphique.
    """
    condition = True  # Condition de boucle pour continuer l'exécution
    if graphique == 0:
        # Si l'option graphique est 0, lance la mise à jour du monde sans interface graphique dans un thread séparé
        threading.Thread(target=update_sans_graphique).start()
    elif graphique == 1:
        # Si l'option graphique est 1, lance la mise à jour avec interface graphique en 2D dans un thread séparé
        threading.Thread(target=update).start()
        # Attend un court laps de temps pour que l'interface graphique se prépare avant de démarrer la stratégie
        time.sleep(1.5)
    elif graphique == 2:
        # Si l'option graphique est 2, laisser passer (utilisé pour l'interface graphique en 3D)
        time.sleep(1.5)
        pass
    
    strat.start()  # Démarre l'exécution de la stratégie
    
    while condition:
        debut = time.time()  # Enregistre le temps de début de chaque boucle
        strat.step()  # Exécute une étape de la stratégie
        
        if GRAPH == 0:
            # Si l'option graphique est 0, affiche les coordonnées du robot
            print(robot.x, robot.y, robot.z)
            
        # Vérifie si la stratégie doit s'arrêter ou si le robot a rencontré un obstacle
        if strat.stop() or robot.crash:
            robot.setVitesse(0, 0)  # Arrête le robot
            robot.stopRec()  # Arrête l'enregistrement de données du robot
            condition = False  # Met fin à la boucle principale
            
        # Attend le temps nécessaire pour maintenir le taux de rafraîchissement du programme
        time.sleep(time.time() - debut)


# Lancement de la stratégie pour tracer un carré
threading.Thread(target=run, args= (TracerCarre(50,robot),GRAPH)).start()
#run(AvancerToutDroit(50,robot),True)
#run(Tourner(math.pi/2,robot),True)

try:
    # Vérifie si l'option graphique est 2 (graphique en 3D)
    if GRAPH == 2:
        # Lancement de la simulation en 3D
        game = MyRobot(monde, tracer_carre)
        # Ajoute la tâche d'actualisation en 3D à la liste des tâches de la simulation
        game.taskMgr.add(update3D, "updateTask")
        # Démarre la simulation de la classe MyRobot
        game.run()
except NameError:
    # Si une erreur de type NameError se produit (par exemple, si la classe MyRobot n'est pas définie), ignore l'erreur
    pass

try:
    # Vérifie si une interface graphique a été créée et démarre la boucle principale de l'interface graphique
    fenetre.mainloop()
except NameError:
    # Si une erreur de type NameError se produit (par exemple, si la fenêtre Tkinter n'est pas définie), ignore l'erreur
    pass
