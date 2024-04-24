import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.graphique.graphique import Graphique
from src.controleur.strategie import *
import math
import time
import threading

# Création du robot
robot = Robot.creation_robot()

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde = monde
monde.place_obstacle()

class Graphique3D:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulation 3D")

        # Création du graphique 3D matplotlib
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Création du canevas Tkinter pour intégrer le graphique 3D matplotlib
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Lancement de l'animation
        self.animation()

    def draw_robot(self):
        # Coordonnées du robot
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

    def animation(self):
        # Supprime les graphiques précédents
        self.ax.clear()

        # Trace la trajectoire en 3D
        t = np.linspace(0, 10, 100)
        x = np.sin(t)
        y = np.cos(t)
        z = t
        self.ax.plot(x, y, z)

        # Ajout du robot dans le graphique 3D
        self.draw_robot()

        # Définit les étiquettes des axes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')

        # Définit l'origine du repère à (0,0,0)
        self.ax.set_xlim([-monde.ligne, monde.ligne])
        self.ax.set_ylim([-monde.colonne, monde.colonne])
        self.ax.set_zlim([0, monde.colonne])

        # Met à jour le graphique
        self.canvas.draw()

        # Appelle cette fonction à nouveau après un certain délai
        self.master.after(100, self.animation)

def main():
    root = tk.Tk()
    app = Graphique3D(root)
    root.mainloop()

if __name__ == "__main__":
    main()
