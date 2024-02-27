import math
import random


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
        self.longueur=longueur
        Obstacle.obstacle_crees += 1

    def getPosition(self):
        """retourne la position d'un obstacle"""
        return self.x, self.y
    
    def getRect(self):
       return [[self.x-self.largeur/2 ,self.y-self.longeur/2], [self.x+self.largeur/2 ,self.y-self.longeur/2], [self.x+self.largeur/2 ,self.y+self.longeur/2], [ self.x-self.largeur/2 ,self.y+self.longeur/2]]



class Mur :
     def __init__(self, x, y, largeur, longueur):
        """Classe heritant de la classe obstacle pour representer un Mur"""
        Obstacle.__init__(self,x,y,largeur,longueur)