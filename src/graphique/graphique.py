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
        self.dessineObstacle()
        self.dessineRobot()
        
    def coordonneesRobot(self, robot):
        """Calcule les coordonnees du robot en fonction de son angle de rotation"""
        cos_dir = math.cos(robot.dir)
        sin_dir = math.sin(robot.dir)

        # Coordonnées du robot
        points = [
            (robot.x + robot.largeur / 2 * sin_dir - robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y + robot.largeur / 2 * cos_dir + robot.longueur / 2 * sin_dir),
            (robot.x - robot.largeur / 2 * sin_dir - robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y - robot.largeur / 2 * cos_dir + robot.longueur / 2 * sin_dir),
            (robot.x - robot.largeur / 2 * sin_dir + robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y - robot.largeur / 2 * cos_dir - robot.longueur / 2 * sin_dir),
            (robot.x + robot.largeur / 2 * sin_dir + robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y + robot.largeur / 2 * cos_dir - robot.longueur / 2 * sin_dir)
        ]

        return points

    def dessineRobot(self):
        """Calcule et dessine le robot sur la fenetre"""
        robot = self.monde.robot
        points = self.coordonneesRobot(robot)

        self.rectangle = self.cnv.create_polygon(*points, fill="blue", outline="black", tags="rectangle") # corps du robot
        self.head = self.cnv.create_line(points[2], points[3], fill="red", width=2, tags="head") # tete du robot

    def deplaceRobot(self):
        """Deplace le robot dans la fenetre"""
        robot = self.monde.robot
        points = self.coordonneesRobot(robot)

        # déplacement du robot
        self.cnv.coords(self.rectangle, *sum(points, ())) 
        self.cnv.coords(self.head, points[2][0], points[2][1], points[3][0], points[3][1]) 
        
    def dessineObstacle(self):
        """Ajoute les obstacles dans la simulation."""
        for obs in self.monde.obstacles:
            self.cnv.create_rectangle(obs.x-obs.longueur/2,self.monde.colonne-obs.y-obs.largeur/2,
                                      obs.x+obs.longueur/2,self.monde.colonne-obs.y+obs.largeur/2,
                                      fill="grey")
            coord_text = f"({obs.x}, {obs.y})"
            self.cnv.create_text(obs.x, self.monde.colonne - obs.y, text=coord_text, anchor=NW, fill="black")


    def update(self):
        """Met à jour l'affichage."""
        self.deplaceRobot()
        self.dessineTrait()
        self.fenetre.update()

    def dessineTrait (self):
        """Dessine un trait en fonction du chemin du robot"""
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