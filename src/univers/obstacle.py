import math
import random

class Obstacle: 
    """
    Classe pour représenter un obstacle dans l'environnement.
    
    Attributs de classe :
    obstacle_crees : Compteur du nombre total d'obstacles créés
    """
    obstacle_crees = 0 

    def __init__(self, x, y, z, largeur, longueur, hauteur): 
        """
        Initialise un nouvel obstacle.
        
        Arguments:
        x : Coordonnée x de l'obstacle 
        y : Coordonnée y de l'obstacle
        z : Coordonnée z de l'obstacle
        largeur : Largeur de l'obstacle
        longueur : Longueur de l'obstacle
        hauteur : Hauteur de l'obstacle
        """
        self.x = x
        self.y = y
        self.z = z
        self.largeur = largeur
        self.longueur = longueur
        self.hauteur = hauteur
        Obstacle.obstacle_crees += 1

    def getPosition(self):
        """
        Retourne la position de l'obstacle.
        
        Retourne:
        Un tuple contenant les coordonnées (x, y) de l'obstacle.
        """
        return self.x, self.y
    
    def getRect(self):
        """
        Renvoie les coordonnées du rectangle représentant l'obstacle.
        
        Retourne:
        Une liste de quatre tuples, chacun représentant un sommet du rectangle
        dans l'ordre suivant : bas-gauche, bas-droit, haut-droit, haut-gauche.
        """
        return [
            [self.x - self.longueur / 2, self.y - self.largeur / 2],  # Bas-gauche
            [self.x + self.longueur / 2, self.y - self.largeur / 2],  # Bas-droit
            [self.x + self.longueur / 2, self.y + self.largeur / 2],  # Haut-droit
            [self.x - self.longueur / 2, self.y + self.largeur / 2]   # Haut-gauche
            ]
