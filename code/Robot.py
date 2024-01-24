class Robot:
    def __init__(self,x,y,vitesse=0): # Constructeur
        self.vitesse=vitesse
        self.x=x
        self.y=y
        pass
    pass

    def avancer(self,m, x1,y1):
        """fonction qui fait avancer le robot"""
        if (self.x + x1 >= m.ligne) or (self.y + y1 >= m.colonne): # test si le deplacement est possible 
            return "mur"
        else:
            self.x += x1
            self.y += y1