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
    def dessineRobot(self,canvas):
        """Dessine un robot sur le canvas avec les coordonnées et la direction spécifiées
        canvas: Le canvas sur lequel le robot doit être dessiné
        robot: L'objet représentant le robot avec les attributs x, y, dir, largeur et longueur.
        """
        canvas.delete("rectangle")
        robot=self.monde.robot
        cos_robot=math.cos(robot.dir)
        sin_robot=math.sin(robot.dir)
        canvas.create_polygon(robot.x+robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                            robot.x-robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                            robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            fill="blue",tags="rectangle")
        canvas.create_line(robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            fill="red",tags="rectangle")
        
    def dessineObstacle (self):
        o1=Obstacle(150,150,50,50)
        self.monde.obstacles.append(o1)

        m1=Obstacle(3,3,1,500) # mur en haut 
        m2=Obstacle(3,3,500,1) # mur gauche
        m3=Obstacle(500,500,500,3) # mur en bas
        m4=Obstacle(500,500,1,500) # mur droit 

        self.monde.obstacles.append(m1)
        self.monde.obstacles.append(m2)
        self.monde.obstacles.append(m3)
        self.monde.obstacles.append(m4)

        for i in self.monde.obstacles:
            self.cnv.create_rectangle(i.x,i.y,i.longueur,i.largeur,fill="grey") #affichage des obstacles


    def update(self):
        # Dessin du robot sur le canevas
        self.dessineRobot(self.cnv)
        self.dessineObstacle()

        