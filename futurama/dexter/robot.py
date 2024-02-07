import sys
import math
import random
import time 

#mettre monde dans self

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse=0, dir=0):
        self.vitesse = vitesse
        self.vg=0 # Vitesse de la roue gauche
        self.vd=0 # Vitesse de la roue droite
        self.nom="dexter"
        self.x = x
        self.y = y
        self.dir = dir % 360 # angle en degré
        self.largeur = largeur # largeur du robot en cm
        self.longueur = longueur # longueur du robot en cm
        self.monde=Monde(20,20)

    def avancer(self, distance):
        """ Avance le robot dans sa direction actuelle """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        if self.monde.peut_avancer(dx, dy,self):
            self.x += dx
            self.y += dy


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


                


