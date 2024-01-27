import math
import random
import time 

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse=0, dir=0):
        self.vitesse = vitesse
        self.x = x
        self.y = y
        self.dir = dir % 360
        self.largeur = largeur
        self.longueur = longueur

    def avancer(self, distance, monde):
        """ Avance le robot dans sa direction actuelle """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        if self.peut_avancer(dx, dy, monde):
            self.x += dx
            self.y += dy

    def reculer(self, distance, monde):
        """ Recule le robot dans sa direction opposée """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        if self.peut_avancer(-dx, -dy, monde):
            self.x -= dx
            self.y -= dy

    def tourner_droite(self, angle):
        """ Tourne le robot vers la droite """
        self.dir = (self.dir - angle) % 360

    def tourner_gauche(self, angle):
        """ Tourne le robot vers la gauche """
        self.dir = (self.dir + angle) % 360

    def peut_avancer(self, dx, dy, monde):
        """ Vérifie si le robot peut avancer sans dépasser les limites du monde """
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < monde.ligne and 0 <= new_y < monde.colonne:
            return True
        return False
    
    def deplacement_vitesse(self,distance,temps,monde):
        """Déplacer le robot dans le monde pendant un n secondes """
        print("le robot commence à se deplacer.")
        debut = time.time()
        vitesse = distance/temps #distance à parcourir sur une seconde
        while time.time()-debut < temps : 
            print("le robot se déplace")
            if self.peut_avancer(self.x+vitesse ,self.y+vitesse, monde):
                self.avancer(vitesse,monde)
            else: 
                self.reculer(vitesse,monde)
            
            monde.affiche()
            time.sleep(vitesse)
            
        print("fin de deplacement")
                


