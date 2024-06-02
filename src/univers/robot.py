import math
import random
import time 

DIR = math.pi  # Définition d'une direction initiale par défaut

class Robot:
    def __init__(self, x, y, z, longueur, largeur, hauteur, vitesse_max, monde=None, dir=0):
        """
        Initialise un objet Robot avec les paramètres spécifiés.
        
        Arguments:
        x (float): La coordonnée x initiale du robot
        y (float): La coordonnée y initiale du robot
        z (float): La coordonnée z initiale du robot
        longueur (float): La longueur du robot en centimètres
        largeur (float): La largeur du robot en centimètres
        hauteur (float): La hauteur du robot en centimètres
        vitesse_max (float): La vitesse maximale du robot
        monde (Monde, optionnel): Le monde dans lequel le robot évolue. Par défaut, None
        dir (float, optionnel): La direction initiale du robot en radians. Par défaut, 0 radian
        """
        self.monde = monde
        self.distanceParcouru = 0
        self.d = largeur  # distance entre les deux roues
        self.crash = False
        self.vitesse_max = vitesse_max
        self.taille_roue = 8
        self.vg = 0  # Vitesse de la roue gauche
        self.vd = 0  # Vitesse de la roue droite
        self.nom = "dexter"
        self.x = x
        self.y = y
        self.z = z
        self.dir = dir % (2 * math.pi)  # angle en radians
        self.largeur = largeur
        self.longueur = longueur
        self.hauteur = hauteur
        self.last_time = time.time()
        self.angle_parcourue = 0

    def getDistanceParcouru(self):
        """Retourne la distance parcourue par le robot."""
        return self.distanceParcouru

    def update(self):
        """
        Met à jour la position et la direction du robot en fonction des vitesses des roues.
        """
        current_time = time.time()  # Obtient le temps actuel
        dt = current_time - self.last_time  # Calcule la différence de temps
        self.last_time = current_time  # Met à jour le temps de la dernière mise à jour
        
        x, y = self.x, self.y
        self.x += ((self.vg * dt + self.vd * dt) / 2.0) * math.cos(self.dir)
        self.y += ((self.vg * dt + self.vd * dt) / 2.0) * math.sin(self.dir)
        
        if self.vg != self.vd:
            denominator = self.vg * dt - self.vd * dt
            if abs(denominator) > 1e-10:  # Vérifie que le dénominateur n'est pas nul
                if abs(self.vg) > abs(self.vd):
                    self.dir -= self.vg * dt / (-self.d * self.vg * dt / denominator)
                    self.angle_parcourue -= self.vg * dt / (-self.d * self.vg * dt / denominator)
                else:
                    self.dir += self.vd * dt / (-self.d * self.vd * dt / denominator)
                    self.angle_parcourue += self.vd * dt / (-self.d * self.vd * dt / denominator)
        
        self.distanceParcouru += math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

    def getRect(self):
        """
        Renvoie les coordonnées des coins du rectangle représentant le robot après rotation.
        
        Retourne:
        Une liste de quatre listes, chaque liste représentant un coin du rectangle après rotation.
        """
        coin1 = [self.x - self.longueur / 2, self.y - self.largeur / 2]
        coin2 = [self.x + self.longueur / 2, self.y - self.largeur / 2]
        coin3 = [self.x + self.longueur / 2, self.y + self.largeur / 2]
        coin4 = [self.x - self.longueur / 2, self.y + self.largeur / 2]

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
        """
        Calcule la distance entre le robot et le prochain obstacle dans sa direction.
        
        Retourne:
        La distance au prochain obstacle en centimètres, jusqu'à un maximum de 150 cm.
        """
        distanceP_capteur = 0
        capteur_x, capteur_y = self.x, self.y
        while not self.monde.detecter_collision(capteur_x, capteur_y):  # Avance le capteur jusqu'à ce qu'il détecte un obstacle
            distanceP_capteur += 1
            if distanceP_capteur > 150:
                return distanceP_capteur
            capteur_x += ((self.vg * 0.01 + self.vd * 0.01) / 2.0) * math.cos(self.dir)
            capteur_y += ((self.vg * 0.01 + self.vd * 0.01) / 2.0) * math.sin(self.dir)
        
        return distanceP_capteur
    
    @staticmethod
    def creation_robot(x, y, z):
        """
        Crée et retourne un nouveau robot avec des paramètres par défaut.
        
        Arguments:
        x (float): La coordonnée x initiale du robot
        y (float): La coordonnée y initiale du robot
        z (float): La coordonnée z initiale du robot
        
        Retourne:
        Un objet Robot.
        """
        return Robot(x, y, z, 20, 20, 20, 40, None, DIR)
    
    def rect(self, x, y):
        """
        Renvoie les coordonnées des coins du rectangle représentant le robot après rotation, pour une position donnée.
        
        Arguments:
        x (float): La coordonnée x du centre du robot
        y (float): La coordonnée y du centre du robot
        
        Retourne:
        Une liste de quatre listes, chaque liste représentant un coin du rectangle après rotation.
        """
        coin1 = [x - self.longueur / 2, y - self.largeur / 2]
        coin2 = [x + self.longueur / 2, y - self.largeur / 2]
        coin3 = [x + self.longueur / 2, y + self.largeur / 2]
        coin4 = [x - self.longueur / 2, y + self.largeur / 2]

        angle_radians = self.dir

        # Rotation des coins du rectangle autour du centre (x, y)
        rotation_coin1 = [x + (coin1[0] - x) * math.cos(angle_radians) - (coin1[1] - y) * math.sin(angle_radians),
                          y + (coin1[0] - x) * math.sin(angle_radians) + (coin1[1] - y) * math.cos(angle_radians)]
        rotation_coin2 = [x + (coin2[0] - x) * math.cos(angle_radians) - (coin2[1] - y) * math.sin(angle_radians),
                          y + (coin2[0] - x) * math.sin(angle_radians) + (coin2[1] - y) * math.cos(angle_radians)]
        rotation_coin3 = [x + (coin3[0] - x) * math.cos(angle_radians) - (coin3[1] - y) * math.sin(angle_radians),
                          y + (coin3[0] - x) * math.sin(angle_radians) + (coin3[1] - y) * math.cos(angle_radians)]
        rotation_coin4 = [x + (coin4[0] - x) * math.cos(angle_radians) - (coin4[1] - y) * math.sin(angle_radians),
                          y + (coin4[0] - x) * math.sin(angle_radians) + (coin4[1] - y) * math.cos(angle_radians)]

        return [rotation_coin1, rotation_coin2, rotation_coin3, rotation_coin4]
    
    def setVitesse(self, vg, vd):
        """
        Définit les vitesses des roues gauche et droite du robot.
        
        Arguments:
        vg (float): La vitesse de la roue gauche
        vd (float): La vitesse de la roue droite
        """
        self.vg = vg
        self.vd = vd
    
    def resetMotor(self, port, angle):
        """Méthode à implémenter : Réinitialise le moteur à un angle donné."""
        pass

    def stopRec(self):
        """Méthode à implémenter : Arrête l'enregistrement."""
        pass

    def getImage(self):
        """Méthode à implémenter : Obtient une image de la caméra du robot."""
        pass
