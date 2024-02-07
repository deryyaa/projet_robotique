import sys
import math
import random
import time 

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse_max, dir=0):
        self.vitesse_max = vitesse_max
        self.taille_roue = 10
        self.vg=4 # Vitesse de la roue gauche
        self.vd=2 # Vitesse de la roue droite
        self.nom="dexter"
        self.x = x
        self.y = y
        self.dir = dir % 360 # angle en degré
        self.largeur = largeur # largeur du robot en cm
        self.longueur = longueur # longueur du robot en cm

    def avancer(self):
        """ Avance le robot dans sa direction actuelle """
        self.vd=self.vitesse_max
        self.vg=self.vitesse_max
        
    def reculer(self):
        """ Recule le robot dans sa direction opposée """
        self.vd=-self.vitesse_max
        self.vg=-self.vitesse_max

    def tourner_droite(self):
        """ Tourne le robot vers la droite """
        self.vd=-self.vitesse_max
        self.vg=self.vitesse_max

    def tourner_gauche(self):
        """ Tourne le robot vers la gauche """
        self.vd=self.vitesse_max
        self.vg=-self.vitesse_max
        
    def mouvement(self, dt):
        self.x += (self.taille_roue*(self.vg+self.vd)/2.0) * math.cos(math.radians(self.dir)) * dt
        self.y -= (self.taille_roue*(self.vg+self.vd)/2.0) * math.sin(math.radians(self.dir)) * dt
        self.dir += (self.vd - self.vg) * dt 
    
    
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


                


