import math
import random
import time 

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse=0, dir=0):
        self.vitesse = vitesse
        self.nom="dexter"
        self.x = x
        self.y = y
        self.dir = dir % 360
        self.largeur = largeur
        self.longueur = longueur

    def avancer(self, distance, monde):
        """ Avance le robot dans sa direction actuelle """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        if monde.peut_avancer(dx, dy,self):
            self.x += dx
            self.y += dy

    def reculer(self, distance, monde):
        """ Recule le robot dans sa direction opposée """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        if monde.peut_avancer(monde,-dx, -dy):
            self.x -= dx
            self.y -= dy

    def tourner_droite(self, angle):
        """ Tourne le robot vers la droite """
        self.dir = (self.dir - angle) % 360

    def tourner_gauche(self, angle):
        """ Tourne le robot vers la gauche """
        self.dir = (self.dir + angle) % 360

    
    
    def vitesse_discrete(self,distance,temps,monde):
        """Déplacer le robot avec une distance dans le monde pendant un temps """
        print("le robot commence a se deplacer.")
        debut = time.time()
        vitesse = distance/temps #distance à parcourir sur une seconde
        duree = temps/distance #temps en seconde à attendre entre chaque déplacement
        while time.time()-debut < temps : 
            if monde.peut_avancer(monde,self.x+vitesse ,self.y+vitesse):
                self.avancer(vitesse,monde)
                monde.affiche()
            time.sleep(duree)
            
        print("fin de deplacement")


                


