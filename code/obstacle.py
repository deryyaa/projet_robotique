import math

class Obstacle: 
    obstacle_crees = 0 

    # obstacle immobile
    def __init__(self,x,y,largeur,longeur): 
        self.x=x
        self.y=y
        self.largeur=largeur
        self.longeur=longeur
        Obstacle.obstacle_crees += 1


