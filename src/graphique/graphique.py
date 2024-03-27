from tkinter import *
from src.univers.monde import Monde
from src.univers.obstacle import *

import math
import time
from threading import Thread

class Graphique(Thread):
    def __init__(self,monde,canvas,fenetre):
        self.monde=monde
        self.fenetre=fenetre
        self.cnv=canvas
        
    def dessineRobot(self):
        """Dessine un robot sur le canvas avec les coordonnées et la direction spécifiées
        canvas: Le canvas sur lequel le robot doit être dessiné
        robot: L'objet représentant le robot avec les attributs x, y, dir, largeur et longueur.
        """
        self.cnv.delete("rectangle")
        self.cnv.delete("head")
        robot = self.monde.robot
        cos_robot = math.cos(robot.dir)
        sin_robot = math.sin(robot.dir)
        
        # Coordonnées des deux points opposés du rectangle
        
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
                            fill="red",tags="head")
        
    def dessineObstacle(self):
        """Ajoute les obstacles dans la simulation."""
        for obs in self.monde.obstacles:
            self.cnv.create_rectangle(obs.x-obs.longueur/2,self.monde.colonne-obs.y-obs.largeur/2,
                                      obs.x+obs.longueur/2,self.monde.colonne-obs.y+obs.largeur/2,
                                      fill="grey")

    def update(self):
        """Met à jour l'affichage."""
        self.dessineRobot()
        #self.dessineTrait()
        self.dessineObstacle()
        self.fenetre.update()

    def dessineTrait (self):
        robot=self.monde.robot
        if not hasattr(self, 'prev_x') or not hasattr(self, 'prev_y'):
            self.prev_x = None
            self.prev_y = None

        if self.prev_x is not None and self.prev_y is not None:
            # Coordonnées du début et de la fin du trait
            x1 = self.prev_x
            y1 = self.monde.colonne - self.prev_y  # Inversion de l'axe y
            x2 = robot.x
            y2 = self.monde.colonne - robot.y  # Inversion de l'axe y

            # Dessiner un trait avec une largeur de 5 pixels
            self.cnv.create_line(x1, y1, x2, y2, width=2)

        # Mettre à jour les coordonnées précédentes du robot
        self.prev_x = robot.x
        self.prev_y = robot.y