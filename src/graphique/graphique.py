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
        o1=Obstacle(150,150,50,50)
        self.monde.obstacles.append(o1)

        for i in self.monde.obstacles:
            self.cnv.create_rectangle(i.x,i.y,i.longueur,i.largeur,fill="grey") #affichage des obstacles

    #def dessineLimites(self):
        #création un carré ou un rectangle qui crée les limites du monde
        #self.monde.setObstacle(Obstacle((5,5,1,600))) #limite à gauche
        #self.monde.setObstacle(Obstacle((5,600,1,600))) #limite à droite
        #self.monde.setObstacle(Obstacle((600,5,1,600))) #limite en haut
        #self.monde.setObstacle(Obstacle((600,600,1,600))) #limite en bas

        #for i in self.monde.obstacles:
            #self.cnv.create_rectangle(i.x-i.longeur/2,i.y-i.largeur/2,i.x+i.longeur/2,i.y+i.largeur/2,fill="grey") #affichage des limites

    def update(self):
        # Dessin du robot sur le canevas
        self.dessineRobot()
        self.dessineObstacle()
        #self.dessineLimites()

        