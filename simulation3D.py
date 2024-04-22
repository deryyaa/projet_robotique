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

FPS=100

#Création de robot
robot = Robot.creation_robot() 

# Création du monde
monde = Monde.creation_monde(robot)
robot.monde=monde
monde.place_obstacle()

fenetre = Tk()
    fenetre.title("Robot dans le monde")
    cnv = Canvas(fenetre, width=monde.ligne, height=monde.colonne, bg="ivory")
    cnv.pack()
    graph=Graphique(monde,cnv,fenetre)
    graph.dessineObstacle()

class Simulation3D:
    def __init__(self, master):
        self.master = master
        self.master.title("Simulation 3D")

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.animation()

    def animation(self):
        # Supprime les graphiques précédents
        self.ax.clear()
        
        # Crée des données pour la simulation
        t = np.linspace(0, 10, 100)
        x = np.sin(t)
        y = np.cos(t)
        z = t
        
        # Trace la trajectoire en 3D
        self.ax.plot(x, y, z)
        
        # Définit les étiquettes des axes
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        
        # Met à jour le graphique
        self.canvas.draw()
        
        # Appelle cette fonction à nouveau après un certain délai
        self.master.after(100, self.animation)

def main():
    root = tk.Tk()
    app = Simulation3D(root)
    root.mainloop()

if __name__ == "__main__":
    main()