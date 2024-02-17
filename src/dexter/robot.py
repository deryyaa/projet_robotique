import sys
import math
import random
import time 

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse_max, direction=[0,0],dir=0):
        """Initialise un objet Robot avec les paramètres spécifiés
        x (float): La coordonnée x initiale du robot
        y (float): La coordonnée y initiale du robot
        longueur (float): La longueur du robot en centimètres
        largeur (float): La largeur du robot en centimètres
        vitesse_max (float): La vitesse maximale du robot
        dir (float, facultatif): La direction initiale du robot en degrés. Par défaut, 0 degré
        """
        self.direction=direction
        self.d=largeur # distance entre les 2 roue
        self.vitesse_max = vitesse_max
        self.taille_roue = 8
        self.vg=0 # Vitesse de la roue gauche
        self.vd=0 # Vitesse de la roue droite
        self.nom="dexter"
        self.x = x
        self.y = y
        self.dir = dir % (2*math.pi) # angle en radians
        self.largeur = largeur # largeur du robot en cm
        self.longueur = longueur # longueur du robot en cm
        self.direction= direction

    
    def move(self,dt):
        """Met à jour la position et la direction du véhicule en fonction des vitesses des roues
        dt : intervalle de temps de rafraichissment (fps)
        """
        self.x += ((self.vg*dt+self.vd*dt)/2.0) * math.cos(self.dir)
        self.y += ((self.vg*dt+self.vd*dt)/2.0) * math.sin(self.dir)
        if(self.vg!=self.vd):
            if(self.vg==0):
                self.dir+=self.vd*dt/(-self.d*self.vd*dt/(self.vg*dt-self.vd*dt))
            elif(self.vd==0):
                self.dir-=self.vg*dt/(-self.d*self.vg*dt/(self.vd*dt-self.vg*dt))
            elif(self.vg>self.vd):
                self.dir-=self.vg*dt/(-self.d*self.vg*dt/(self.vd*dt-self.vg*dt))
            else:
                self.dir+=self.vd*dt/(-self.d*self.vd*dt/(self.vg*dt-self.vd*dt))
                
    
    def capteur_distance(self):
        distanceP_capteur = 0
        capteur_x, capteur_y = self.robot.x, self.robot.y

        while not self.monde.detecter_collision(capteur_x, capteur_y): #tant qu'il n'a rien detecté, on fait avancer le capteur dans la direction de robot et on incremente sa distance parcourue
            distanceP_capteur+= 1
            capteur_x += self.direction[0]
            capteur_y += self.direction[1]

        print(f"Obstacle détecté à : {distanceP_capteur}")
        print(f"Position actuelle du robot : {[self.robot.x, self.robot.y]}, Distance jusqu'à l'obstacle : {distanceP_capteur}")





                


