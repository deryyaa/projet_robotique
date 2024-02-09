import sys
import math
import random
import time 

class Robot:
    def __init__(self, x, y, longueur, largeur, vitesse_max, dir=0):
        """Initialise un objet Robot avec les paramètres spécifiés
        x (float): La coordonnée x initiale du robot
        y (float): La coordonnée y initiale du robot
        longueur (float): La longueur du robot en centimètres
        largeur (float): La largeur du robot en centimètres
        vitesse_max (float): La vitesse maximale du robot
        dir (float, facultatif): La direction initiale du robot en degrés. Par défaut, 0 degré
        """
        self.vitesse_max = vitesse_max
        self.taille_roue = 10
        self.vg=0 # Vitesse de la roue gauche
        self.vd=0 # Vitesse de la roue droite
        self.nom="dexter"
        self.x = x
        self.y = y
        self.dir = dir % 360 # angle en degré
        self.largeur = largeur # largeur du robot en cm
        self.longueur = longueur # longueur du robot en cm

    def avancer_(self, distance, monde):
        """ Avance le robot dans sa direction actuelle """
        dx = distance * math.cos(math.radians(self.dir))
        dy = distance * math.sin(math.radians(self.dir))
        if monde.peut_avancer(dx, dy,self):
            self.x += dx

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
        self.vd=-self.vitesse_maxself.robot.x,
        """ Tourne le robot vers la gauche """
        self.vd=self.vitesse_max
        self.vg=-self.vitesse_max
        
    def augmenter_vg(self,n):
        """Augmente la vitesse de la roue gauche"""
        if(n<0):
            print("n doit être positif")
            exit
        if(self.vg+n>self.vitesse_max):
            self.vg=self.vitesse_max
        else:
            self.vg+=n
    
    def augmenter_vd(self,n):
        """Augmente la vitesse de la roue droite"""
        if(n<0):
            print("n doit être positif")
            exit
        if(self.vd+n>self.vitesse_max):
            self.vd=self.vitesse_max
        else:
            self.vd+=n
    
    def mouvement(self, dt):
        """Met à jour la position et la direction du véhicule en fonction des vitesses des roues"""
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



class CapteurDistance:
    def __init__(self, robot, direction, distance_max):
        self.robot = robot
        self.direction= direction
        self.distance_max= distance_max

    def distance_points(p1, p2):
        """Calcule la distance euclidienne entre deux points"""
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

    def distance(self):
        capteur = [self.robot.x, self.robot.y] # initialise le capteur de distance à la position du robot 
        distanceP_capteur = 0 # initialise la distance parcourue par le capteur à 0

        while distanceP_capteur < self.distance_max:
            # capteur qu'on deplace dans la direction specifiée (self.direction)
            capteur = (capteur[0] + self.direction[0], capteur[1] + self.direction[1])
            distanceP_capteur += 1

            distance_actuelle = distance_points([self.robot.x, self.robot.y], position_obstacle) # calcul distance entre le robot et l'obstacle
            print(f"Position actuelle du robot : {[self.robot.x, self.robot.y]}, Distance jusqu'à l'obstacle : {distance_actuelle}")

            # Vérification si le robot est proche de l'obstacle
            if distance_actuelle < 1:
                print(f"Collision : Obstacle detecté à une distance de {distance_actuelle}")
                break   




                


