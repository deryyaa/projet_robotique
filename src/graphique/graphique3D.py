import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
import math


class Graphique3D:
    def __init__(self, monde, fenetre):
        self.monde = monde
        self.fenetre = fenetre
        self.fenetre.title("Simulation 3D")

        # Création du graphique 3D matplotlib
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        # List to store robot lines
        self.robot_lines = []

        # Création du canevas Tkinter pour intégrer le graphique 3D matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.fenetre)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Lancement de l'animation
        self.graphique()


    def dessineRobot(self):
        # Coordonnées du robot
        robot = self.monde.robot
        x, y, z = robot.x, robot.y, robot.z
        longueur, largeur, hauteur = robot.longueur, robot.largeur, robot.hauteur

        # Dessine les lignes pour former le cube
        edges = [
            [x - longueur / 2, y - largeur / 2, z - hauteur / 2],
            [x + longueur / 2, y - largeur / 2, z - hauteur / 2],
            [x + longueur / 2, y + largeur / 2, z - hauteur / 2],
            [x - longueur / 2, y + largeur / 2, z - hauteur / 2],
            [x - longueur / 2, y - largeur / 2, z + hauteur / 2],
            [x + longueur / 2, y - largeur / 2, z + hauteur / 2],
            [x + longueur / 2, y + largeur / 2, z + hauteur / 2],
            [x - longueur / 2, y + largeur / 2, z + hauteur / 2]
        ]

        # Liste des arêtes qui forment le cube
        edges = [
            [edges[0], edges[1], edges[2], edges[3], edges[0]],
            [edges[4], edges[5], edges[6], edges[7], edges[4]],
            [edges[0], edges[4]],
            [edges[1], edges[5]],
            [edges[2], edges[6]],
            [edges[3], edges[7]]
        ]

        for edge in edges:
            x, y, z = zip(*edge)
            self.ax.plot(x, y, z, color='red')

    def dessineObstacle(self):

        obstacles=self.monde.obstacles

        # Dessiner chaque obstacle
        for obstacle in obstacles:
            # Coordonnées de l'obstacle
            x, y, z = obstacle.x, obstacle.y, obstacle.z
            longueur, largeur, hauteur = obstacle.longueur, obstacle.largeur, obstacle.hauteur

            # Dessiner les lignes pour former le cube de l'obstacle
            edges = [
                [x - longueur / 2, y - largeur / 2, z - hauteur / 2],
                [x + longueur / 2, y - largeur / 2, z - hauteur / 2],
                [x + longueur / 2, y + largeur / 2, z - hauteur / 2],
                [x - longueur / 2, y + largeur / 2, z - hauteur / 2],
                [x - longueur / 2, y - largeur / 2, z + hauteur / 2],
                [x + longueur / 2, y - largeur / 2, z + hauteur / 2],
                [x + longueur / 2, y + largeur / 2, z + hauteur / 2],
                [x - longueur / 2, y + largeur / 2, z + hauteur / 2]
            ]

            # Liste des arêtes qui forment le cube de l'obstacle
            edges = [
                [edges[0], edges[1], edges[2], edges[3], edges[0]],
                [edges[4], edges[5], edges[6], edges[7], edges[4]],
                [edges[0], edges[4]],
                [edges[1], edges[5]],
                [edges[2], edges[6]],
                [edges[3], edges[7]]
            ]

            # Dessiner chaque arête
            for edge in edges:
                x, y, z = zip(*edge)
                self.ax.plot(x, y, z, color='blue')


    def graphique(self):
        # Supprime les graphiques précédents
        self.ax.clear()

        # Trace la trajectoire en 3D
        t = np.linspace(0, 10, 100)
        x = np.sin(t)
        y = np.cos(t)
        z = t
        self.ax.plot(x, y, z)

        # Ajout du robot et des obstacles dans le graphique 3D
        self.dessineRobot()
        self.dessineObstacle()

        # Définit les étiquettes des axes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        # Définit l'origine du repère à (0,0,0)
        self.ax.set_xlim([-self.monde.ligne, self.monde.ligne])
        self.ax.set_ylim([-self.monde.colonne, self.monde.colonne])
        self.ax.set_zlim([0, self.monde.colonne])

        # Met à jour le graphique
        self.canvas.draw()

        # Appelle cette fonction à nouveau après un certain délai
        self.fenetre.after(100, self.graphique)

    def update(self):
        """Met à jour l'affichage."""
        self.deplaceRobot()
        self.fenetre.update()

    def coordonneesRobot(self, robot):
        """Calculate the coordinates of the robot based on its rotation angle."""
        cos_dir = math.cos(robot.dir)
        sin_dir = math.sin(robot.dir)

        # Robot coordinates
        points = [
            (robot.x + robot.largeur / 2 * sin_dir - robot.longueur / 2 * cos_dir, 
            robot.y + robot.largeur / 2 * cos_dir + robot.longueur / 2 * sin_dir, 
            robot.z),  # Front left
            (robot.x - robot.largeur / 2 * sin_dir - robot.longueur / 2 * cos_dir, 
            robot.y - robot.largeur / 2 * cos_dir + robot.longueur / 2 * sin_dir, 
            robot.z),  # Front right
            (robot.x - robot.largeur / 2 * sin_dir + robot.longueur / 2 * cos_dir, 
            robot.y - robot.largeur / 2 * cos_dir - robot.longueur / 2 * sin_dir, 
            robot.z),  # Back right
            (robot.x + robot.largeur / 2 * sin_dir + robot.longueur / 2 * cos_dir, 
            robot.y + robot.largeur / 2 * cos_dir - robot.longueur / 2 * sin_dir, 
            robot.z)   # Back left
        ]

        return points

    def deplaceRobot(self):
        """Move the robot in the window."""
        robot = self.monde.robot
        points = self.coordonneesRobot(robot)

        # Update the coordinates of the robot lines
        for line, edge in zip(self.robot_lines, points):
            x, y, z = edge
            line.set_data_3d(np.array([x]), np.array([y]), np.array([z]))

        self.canvas.draw()
