import sys
import math
import random
import time 

class Robot:
    def __init__(self, x, y, z, longueur, largeur, vitesse_max, monde=None, dir=0):
        """Initialise un objet Robot avec les paramètres spécifiés
        x (float): La coordonnée x initiale du robot
        y (float): La coordonnée y initiale du robot
        longueur (float): La longueur du robot en centimètres
        largeur (float): La largeur du robot en centimètres
        vitesse_max (float): La vitesse maximale du robot
        dir (float, facultatif): La direction initiale du robot en degrés. Par défaut, 0 degré
        """
        self.monde=monde
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
        self.z=z
        self.dir = dir % (2*math.pi) # angle en radians
        self.largeur = largeur # largeur du robot en cm
        self.longueur = longueur # longueur du robot en cm
        self.last_time=time.time()
        self.angle_parcourue=0

    def getDistanceParcouru(self):
        return self.distanceParcouru
    


    def update(self):
        """Met à jour la position et la direction du véhicule en fonction des vitesses des roues
        dt : intervalle de temps de rafraichissment (fps)
        """
        current_time = time.time()  # Obtient le temps actuel
        dt = current_time - self.last_time  # Calcule la différence de temps
        self.last_time = current_time  # Met à jour le temps de la dernière mise à jour
        
        x=self.x
        y=self.y
        self.x += ((self.vg*dt+self.vd*dt)/2.0) * math.cos(self.dir)
        self.y += ((self.vg*dt+self.vd*dt)/2.0) * math.sin(self.dir)
        if(self.vg!=self.vd):
            if(abs(self.vg)>abs(self.vd)):
                self.dir-=self.vg*dt/(-self.d*self.vg*dt/(self.vd*dt-self.vg*dt))
                self.angle_parcourue-=self.vg*dt/(-self.d*self.vg*dt/(self.vd*dt-self.vg*dt))
            else:
                self.dir+=self.vd*dt/(-self.d*self.vd*dt/(self.vg*dt-self.vd*dt))
                self.angle_parcourue+=self.vd*dt/(-self.d*self.vd*dt/(self.vg*dt-self.vd*dt))
        self.distanceParcouru+=math.sqrt((self.x-x)**2+(self.y-y)**2)
    
    def getRect(self):
        coin1 = [self.x - self.longueur / 2, self.y - self.largeur / 2]
        coin2 = [self.x + self.longueur / 2, self.y - self.largeur / 2]
        coin3 = [self.x + self.longueur / 2, self.y + self.largeur / 2]
        coin4 = [self.x - self.longueur / 2, self.y + self.largeur / 2]

        # Ajout de l'angle du robot (en degrés)  
        angle_radians = self.dir


        # Rotation des coins du rectangle autour du centre (self.x, self.y)
        rotation_coin1 = [self.x + (coin1[0] - self.x) * math.cos(angle_radians) - (coin1[1] - self.y) * math.sin(angle_radians),
            self.y + (coin1[0] - self.x) * math.sin(angle_radians) + (coin1[1] - self.y) * math.cos(angle_radians)]
        rotation_coin2 = [self.x + (coin2[0] - self.x) * math.cos(angle_radians) - (coin2[1] - self.y) * math.sin(angle_radians),
            self.y + (coin2[0] - self.x) * math.sin(angle_radians) + (coin2[1] - self.y) * math.cos(angle_radians)]
        rotation_coin3 = [self.x + (coin3[0] - self.x) * math.cos(angle_radians) - (coin3[1] - self.y) * math.sin(angle_radians),
            self.y + (coin3[0] - self.x) * math.sin(angle_radians) + (coin3[1] - self.y) * math.cos(angle_radians)]
        rotation_coin4 = [self.x + (coin4[0] - self.x) * math.cos(angle_radians) - (coin4[1] - self.y) * math.sin(angle_radians),
            self.y + (coin4[0] - self.x) * math.sin(angle_radians) + (coin4[1] - self.y) * math.cos(angle_radians)]

        return [rotation_coin1, rotation_coin2, rotation_coin3, rotation_coin4]

    def capteur_distance(self):
        distanceP_capteur = 0
        capteur_x = self.x
        capteur_y = self.y
        while not self.monde.detecter_collision(capteur_x,capteur_y): #tant qu'il n'a rien detecté, on fait avancer le capteur dans la direction de robot et on incremente sa distance parcourue
            distanceP_capteur+= 1
            if distanceP_capteur>150:
                return distanceP_capteur
            capteur_x += ((self.vg*0.01+self.vd*0.01)/2.0) * math.cos(self.dir)
            capteur_y += ((self.vg*0.01+self.vd*0.01)/2.0) * math.sin(self.dir)
        
        return distanceP_capteur
    
    def creation_robot():
        """ Creation d'un robot"""
        robot = Robot(320, 320, 0, 20, 15 , 40, None,math.pi/4)
        return robot
    
    def rect(self,x,y):
        coin1 = [x - self.longueur / 2, y - self.largeur / 2]
        coin2 = [x + self.longueur / 2, y - self.largeur / 2]
        coin3 = [x + self.longueur / 2, y + self.largeur / 2]
        coin4 = [x - self.longueur / 2, y + self.largeur / 2]

        # Ajout de l'angle du robot (en degrés)  
        angle_radians = self.dir


        # Rotation des coins du rectangle autour du centre (self.x, self.y)
        rotation_coin1 = [x + (coin1[0] - x) * math.cos(angle_radians) - (coin1[1] - y) * math.sin(angle_radians),
            y + (coin1[0] - x) * math.sin(angle_radians) + (coin1[1] - y) * math.cos(angle_radians)]
        rotation_coin2 = [x + (coin2[0] - x) * math.cos(angle_radians) - (coin2[1] - y) * math.sin(angle_radians),
            y + (coin2[0] - x) * math.sin(angle_radians) + (coin2[1] - y) * math.cos(angle_radians)]
        rotation_coin3 = [x + (coin3[0] - x) * math.cos(angle_radians) - (coin3[1] - y) * math.sin(angle_radians),
            y + (coin3[0] - x) * math.sin(angle_radians) + (coin3[1] - y) * math.cos(angle_radians)]
        rotation_coin4 = [x + (coin4[0] - x) * math.cos(angle_radians) - (coin4[1] - y) * math.sin(angle_radians),
            y + (coin4[0] - x) * math.sin(angle_radians) + (coin4[1] - y) * math.cos(angle_radians)]

        return [rotation_coin1, rotation_coin2, rotation_coin3, rotation_coin4]
    
    def setVitesse(self,vg,vd):
        self.vg=vg
        self.vd=vd