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

    def distance_points(p1, p2):
    """Calcule la distance euclidienne entre deux points"""
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

"""PAS FINIT """
position_robot = [self.x, self.y]  # position initiale du robot
position_obstacle = [obstacle.x, obstacle.y]  # position de l'obstacle 
vecteur_d = [1, 1]  # vecteur de deplacement 
distance_parcourue = 0  # distance parcourue par le robot

while True:
    # mise à jour de la position du robot selon le vecteur de déplacement
    position_robot[0] += vecteur_d[0]
    position_robot[1] += vecteur_d[1]
    
    distance_actuelle = distance_points(position_robot, position_obstacle) # calcul distance entre le robot et l'obstacle
    print(f"Position actuelle du robot : {position_robot}, Distance jusqu'à l'obstacle : {distance_actuelle}")
    
    # Vérification si le robot est suffisamment proche de l'obstacle
    if distance_actuelle < 1:
        print(f"Collision : Obstacle detecté à une distance de {distance_actuelle}")
        break


                


