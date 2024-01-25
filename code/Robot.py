from math import math
class Robot:
    def __init__(self,x,y,vitesse=0,dir=0): # Constructeur
        self.vitesse=vitesse
        self.x=x
        self.y=y
        self.dir=dir

    def avancer(self,m, x1,y1):
        """fonction qui fait avancer le robot"""
        if (self.x + x1 >= m.ligne) or (self.y + y1 >= m.colonne): # test si le deplacement est possible 
            return "mur"
        else:
            self.x += x1
            self.y += y1
    def avance(self,m):
        if (self.x+self.vitesse*math.cos(self.dir)>=m.ligne) or (self.y+self.vitesse*math.sin(self.dir)>=m.colonne):
            return "mur"
        else:
            self.x=self.x+self.vitesse*math.cos(self.dir)
            self.y=self.y+self.vitesse*math.sin(self.dir)
    def tourne(self,angle):
        self.dir=(self.dir+angle)%(2*math.PI)