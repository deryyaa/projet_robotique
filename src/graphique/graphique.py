from tkinter import *
from src.univers.monde import Monde
from src.univers.obstacle import *

import math
import time
from threading import Thread

class Graphique(Thread):
    """
    Cette classe gère l'affichage graphique du monde et du robot sur une interface Tkinter.
    Hérite de Thread pour permettre l'exécution en parallèle avec d'autres processus.

    """
    def __init__(self,monde,canvas,fenetre):
        """
        Initialise l'objet Graphique avec le monde, le canvas et la fenêtre donnés.
        Dessine initialement les obstacles et le robot sur le canvas, et configure le label des coordonnées.
        """
        self.monde=monde # Attribue le monde 
        self.fenetre=fenetre # Attribue une fenetre graphique, l'interface où les éléments seront affichés
        self.cnv=canvas # Attribue un canvas, une toile sur laquelle on peut dessiner des éléments graphiques
        self.dessineObstacle() # Appelle la méthode pour dessiner les obstacles sur le canvas
        self.dessineRobot() # Appelle la méthode pour dessiner le robot sur le canvas
        self.coord_label = Label(fenetre, text="")  
        # Crée un widget Label dans la fenêtre (fenetre) pour afficher du texte, initialement vide
        self.coord_label.pack()  
        # Ajoute le label à la fenêtre graphique et l'affiche à l'écran


    def coordonneesRobot(self, robot):
        """Calcule les coordonnees du robot en fonction de son angle de rotation"""
        # Calcul des valeurs du cosinus et du sinus de l'angle de rotation du robot
        cos_dir = math.cos(robot.dir)
        sin_dir = math.sin(robot.dir)

        # Coordonnées du robot
        points = [
            # Calcul des coordonnées du coin avant-droit du robot
            (robot.x + robot.largeur / 2 * sin_dir - robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y + robot.largeur / 2 * cos_dir + robot.longueur / 2 * sin_dir),

            # Calcul des coordonnées du coin arrière-droit du robot
            (robot.x - robot.largeur / 2 * sin_dir - robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y - robot.largeur / 2 * cos_dir + robot.longueur / 2 * sin_dir),
            
            # Calcul des coordonnées du coin arrière-gauche du robot
            (robot.x - robot.largeur / 2 * sin_dir + robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y - robot.largeur / 2 * cos_dir - robot.longueur / 2 * sin_dir),
            
            # Calcul des coordonnées du coin avant-gauche du robot
            (robot.x + robot.largeur / 2 * sin_dir + robot.longueur / 2 * cos_dir, self.monde.colonne - robot.y + robot.largeur / 2 * cos_dir - robot.longueur / 2 * sin_dir)
        ]

        return points # Retourne une liste de tuples, chaque tuple représente les coordonnées (x, y)

    def dessineRobot(self):
        """Calcule et dessine le robot sur la fenetre"""
        # Récupération de l'objet robot depuis l'attribut monde
        robot = self.monde.robot
        
        # Calcul des coordonnées des coins du robot
        points = self.coordonneesRobot(robot)

        # Dessin du corps du robot
        # *points décompose la liste des coordonnées en arguments individuels
        # fill="blue" définit la couleur de remplissage du polygone
        # outline="black" définit la couleur du contour du polygone
        # tags="rectangle" permet d'associer un tag "rectangle" à cet élément graphique, utile pour manipuler l'élément plus tard
        self.rectangle = self.cnv.create_polygon(*points, fill="blue", outline="black", tags="rectangle") # corps du robot
        
        # Dessin de la tête du robot
        # points[2] et points[3] sont les coordonnées des coins arrière-gauche et avant-gauche du robot
        # fill="red" définit la couleur de la ligne
        # width=2 définit l'épaisseur de la ligne
        # tags="head" permet d'associer un tag "head" à cet élément graphique, utile pour manipuler l'élément plus tard
        self.head = self.cnv.create_line(points[2], points[3], fill="red", width=2, tags="head") # tete du robot

    def deplaceRobot(self):
        """Deplace le robot dans la fenetre"""
        # Récupération de l'objet robot depuis l'attribut monde
        robot = self.monde.robot
        
        # Calcul des coordonnées des coins du robot
        points = self.coordonneesRobot(robot)

        # Déplacement du corps du robot
        # La méthode coords de canvas est utilisée pour mettre à jour les coordonnées d'un polygone existant
        # *sum(points, ()) aplatit la liste des tuples de coordonnées en une liste simple
        self.cnv.coords(self.rectangle, *sum(points, ())) 
        
        # Déplacement de la tête du robot
        # La méthode coords de canvas est utilisée pour mettre à jour les coordonnées d'une ligne existante
        # points[2][0], points[2][1], points[3][0], points[3][1] sont les nouvelles coordonnées de la ligne
        self.cnv.coords(self.head, points[2][0], points[2][1], points[3][0], points[3][1]) 
        
    def dessineObstacle(self):
        """Ajoute les obstacles dans la simulation."""
        # Parcours de la liste des obstacles dans le monde
        for obs in self.monde.obstacles:
            # Création d'un rectangle pour représenter l'obstacle
            # Les coordonnées du rectangle sont calculées en fonction de la position et des dimensions de l'obstacle
            # Le rectangle est rempli avec la couleur "grey"
            self.cnv.create_rectangle(obs.x-obs.longueur/2,self.monde.colonne-obs.y-obs.largeur/2,
                                      obs.x+obs.longueur/2,self.monde.colonne-obs.y+obs.largeur/2,
                                      fill="grey")
            # Création du texte pour afficher les coordonnées de l'obstacle
            coord_text = f"({obs.x}, {obs.y})"
            self.cnv.create_text(
                obs.x,  # Position x du texte
                self.monde.colonne - obs.y,  # Position y du texte (inversée)
                text=coord_text,  # Texte à afficher
                anchor=NW,  # Ancrage du texte au coin supérieur gauche
                fill="black"  # Couleur du texte en noir
            )

    def update(self):
        """Met à jour l'affichage."""
         # Déplace le robot selon sa nouvelle position
        # Cette ligne appelle la méthode deplaceRobot pour mettre à jour la position graphique du robot sur le canvas
        self.deplaceRobot()
        
        # Dessine le trait représentant le chemin parcouru par le robot
        # Cette ligne appelle la méthode dessineTrait pour tracer le chemin que le robot a parcouru
        self.dessineTrait()
        
        # Met à jour l'affichage de la fenêtre
        # Cette ligne force une mise à jour de l'affichage de la fenêtre pour refléter les changements
        self.fenetre.update()
        
        # Met à jour le label des coordonnées du robot
        # Cette ligne appelle la méthode updateCoordLabel pour mettre à jour le texte affiché des coordonnées du robot
        self.updateCoordLabel()

    def dessineTrait (self):
        """Dessine un trait en fonction du chemin du robot"""
        # Récupération de l'objet robot depuis l'attribut monde
        robot=self.monde.robot

        # Vérification de l'existence des coordonnées précédentes du robot
        if not hasattr(self, 'prev_x') or not hasattr(self, 'prev_y'):
            # Si les coordonnées précédentes n'existent pas, les initialiser à None
            self.prev_x = None
            self.prev_y = None

        # Si les coordonnées précédentes existent et ne sont pas None
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

    def updateCoordLabel(self):
        """Met à jour le label des coordonnées du robot"""
        # Récupération de l'objet robot depuis l'attribut monde
        robot = self.monde.robot

        # Création d'un texte formaté avec les coordonnées actuelles du robot
        coord_text = f"coordonnées robot : x = {robot.x:.2f}, y = {robot.y:.2f}"

        # Mise à jour du texte du label avec les nouvelles coordonnées du robot
        # La méthode config est utilisée pour changer la configuration du label, ici on change le texte affiché
        self.coord_label.config(text=coord_text)