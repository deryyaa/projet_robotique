import math
import unittest

class Obstacle: 
    """ Classe pour représenter un obstacle dans l'environnement.

        :var classe obstacle_crees: Compteur du nombre total d'obstacles créés
    """
    obstacle_crees = 0 

    # obstacle immobile
    def __init__(self,x,y,largeur,longueur): 
        """Initialise un nouvel obstacle.
        :param x: Coordonnée x de l'obstacle 
        :param y:Coordonnée y de l'obstacle
        :param largeur: Dimension de l'obsatcle  
        :param longueur: Dimension de l'obsatcle """

        self.x=x
        self.y=y
        self.largeur=largeur
        self.longeur=longueur
        Obstacle.obstacle_crees += 1

