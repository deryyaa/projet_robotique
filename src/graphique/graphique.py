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
        robot=self.monde.robot
        #canvas.delete("rectangle")
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
    def update(self):
        # Dessin du robot sur le canevas
        self.dessineRobot(self.cnv)

    def dessineObstacle (self):
        #création de 2 obstacle 
        for i in range(2):
            self.monde.setObstacle(Obstacle(2+(i+1)*100, 40, 50, 50)) # Creation de plusieurs obstacle
        for i in self.monde.obstacles:
            print(i.x,i.y)
            self.cnv.create_rectangle(i.x-i.longeur/2,i.y-i.largeur/2,i.x+i.longeur/2,i.y+i.largeur/2,fill="grey") #affichage des 2 obstacles