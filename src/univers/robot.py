import sys
import math
import random
import time 
from src.univers.monde import Monde

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse_max,dir=0):
        """Initialise un objet Robot avec les paramètres spécifiés
        x (float): La coordonnée x initiale du robot
        y (float): La coordonnée y initiale du robot
        longueur (float): La longueur du robot en centimètres
        largeur (float): La largeur du robot en centimètres
        vitesse_max (float): La vitesse maximale du robot
        dir (float, facultatif): La direction initiale du robot en degrés. Par défaut, 0 degré
        """
        self.distanceParcouru=0
        self.d=largeur # distance entre les 2 roue
        self.crash=False
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

    
    def move(self,dt):
        """Met à jour la position et la direction du véhicule en fonction des vitesses des roues
        dt : intervalle de temps de rafraichissment (fps)
        """
        x=self.x
        y=self.y
        self.x += ((self.vg*dt+self.vd*dt)/2.0) * math.cos(self.dir)
        self.y += ((self.vg*dt+self.vd*dt)/2.0) * math.sin(self.dir)
        if(self.vg!=self.vd):
            if(abs(self.vg)>abs(self.vd)):
                self.dir-=self.vg*dt/(-self.d*self.vg*dt/(self.vd*dt-self.vg*dt))
            else:
                self.dir+=self.vd*dt/(-self.d*self.vd*dt/(self.vg*dt-self.vd*dt))
        self.distanceParcouru+=math.sqrt((self.x-x)**2+(self.y-y)**2)
        #print(self.distanceParcouru)
    
    def getDistanceParcouru(self):
        return self.distanceParcouru
        
    def getRect(self):
       return [[self.x-self.longueur/2 ,self.y-self.largeur/2], [self.x+self.longueur/2 ,self.y-self.largeur/2], [self.x+self.longueur/2 ,self.y+self.largeur/2], [ self.x-self.longueur/2 ,self.y+self.largeur/2]]

    def getPosition(self):
        return (self.x,self.y)
    
    def setVitesse(self,vg,vd):
        self.vg=vg
        self.vd=vd
        

    def capteur_distance(self,monde):
        distanceP_capteur = 0
        capteur_x = self.x
        capteur_y = self.y

        while not monde.detecter_collision(capteur_x, capteur_y): #tant qu'il n'a rien detecté, on fait avancer le capteur dans la direction de robot et on incremente sa distance parcourue
            distanceP_capteur+= 0.1
            if distanceP_capteur>50:
                print(f"Position actuelle du robot : {[self.x, self.y]}, Distance jusqu'a l'obstacle : {distanceP_capteur}")
                return distanceP_capteur  
            capteur_x += ((self.vg*0.01+self.vd*0.01)/2.0) * math.cos(self.dir)
            capteur_y += ((self.vg*0.01+self.vd*0.01)/2.0) * math.sin(self.dir)
            
        print(f"Position actuelle du robot : {[self.x, self.y]}, Distance jusqu'a l'obstacle : {distanceP_capteur}")
        return distanceP_capteur
        