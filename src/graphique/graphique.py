from tkinter import *
from src.univers.monde import Monde
from src.univers.obstacle import *

import math
import time
from threading import Thread

class Graphique(Thread):
    def __init__(self,monde,canvas, FPS=100):
        self.monde=monde
        self.FPS=FPS
        self.cnv=canvas
    def dessineRobot(self):
        """Dessine un robot sur le canvas avec les coordonnées et la direction spécifiées
        canvas: Le canvas sur lequel le robot doit être dessiné
        robot: L'objet représentant le robot avec les attributs x, y, dir, largeur et longueur.
        """
        self.cnv.delete("rectangle")
        robot=self.monde.robot
        cos_robot=math.cos(robot.dir)
        sin_robot=math.sin(robot.dir)
        self.cnv.create_polygon(robot.x+robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                            robot.x-robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                            robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            fill="blue",tags="rectangle")
        self.cnv.create_line(robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            fill="red",tags="rectangle")
        
    def dessineObstacle (self):
        """
        Dessine les obstacles dans la simulation.
        """
        self.monde.creation_obstacle(380,200,50,50)
        #créer un obstacle et ajout à la liste d'obstacle
        

        #créer les limites du monde et ajout à la liste d'obstacle
        self.monde.creation_obstacle(250,1,1,500) # mur du bas 
        self.monde.creation_obstacle(1,250,500,1) # mur du gauche
        self.monde.creation_obstacle(250,499,1,500) # mur du haut
        self.monde.creation_obstacle(500,250,500,1) # mur du droit 

        #self.monde.obstacles.append(m1)
        #self.monde.obstacles.append(m2)
        #self.monde.obstacles.append(m3)
        #self.monde.obstacles.append(m4)

        #affichage des obstacles
        for i in self.monde.obstacles:
            self.cnv.create_rectangle(i.x-i.longueur/2,self.monde.colonne-i.y-i.largeur/2,i.x+i.longueur/2,self.monde.colonne-i.y+i.largeur/2,fill="grey") #affichage des obstacles


    def update(self):
        # Dessin du robot sur le canevas
        self.dessineRobot()

        