import math

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse=0, dir=0):
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.dir = dir % 360
        self.largeur = largeur
        self.longueur = longueur

    def avancer(self, distance):
        """ Avance le robot dans sa direction actuelle """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        self.x += dx
        self.y += dy

    def reculer(self, distance):
        """ Recule le robot dans sa direction opposée """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        self.x -= dx
        self.y -= dy

    def tourner_droite(self, angle):
        """ Tourne le robot vers la droite """
        self.dir = (self.dir - angle) % 360

    def tourner_gauche(self, angle):
        """ Tourne le robot vers la gauche """
        self.dir = (self.dir + angle) % 360