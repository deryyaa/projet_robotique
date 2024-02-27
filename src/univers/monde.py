from src.univers.obstacle import Obstacle
from threading import Thread

class Monde(Thread):
    def __init__(self, ligne, colonne):
        """ constructeur """
        self.ligne = ligne  # initialisation des coordonnées
        self.colonne = colonne
        self.robot = None
        self.obstacles = [] #création de la liste d'obstacle

    def detecter_collision(self,x,y):
        """Renvoie true s'il y a collision entre un point et un des obstacles du monde, false sinon"""
        for obst in self.obstacles:
            # Verifie si collision entre point et obstacle
            if (x >= obst.x and x <= obst.x + obst.longueur and
            y >= obst.y and y <= obst.y + obst.largeur): 
                return True
        return False
    
    def update(self,robot):
        self.robot=robot


def collision_rect(r1, r2):
    """Vérifie si deux rectangles se superposent

    Return True si les rectangles se superposent, False sinon.
    """
    # Prend en parametre une liste de tuple des 2 coordonnées des rectangles (obstacle et robot)
    # Déballage des tuples pour obtenir les coordonnées et dimensions des rectangles
    x1, y1, w1, h1 = r1[0][0], r1[0][1], r1[1][0] - r1[0][0], r1[1][1] - r1[0][1]
    x2, y2, w2, h2 = r2[0][0], r2[0][1], r2[1][0] - r2[0][0], r2[1][1] - r2[0][1]
    
    # Vérification de la superposition des rectangles
    # La superposition est vérifiée en négatif, donc si l'une des conditions est vraie, la superposition n'a pas lieu.
    return not (x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2)
