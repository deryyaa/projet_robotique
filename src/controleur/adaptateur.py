from src.controleur.robotReel import Robot2IN013_Mockup
import math
import time

class Robot2I013Adaptateur():
    """
    Classe adaptatrice pour un robot de type 2I013, permettant de contrôler le robot et de gérer ses états.

    Attributs:
    
    monde (Object) : Référence au monde dans lequel le robot évolue (peut être None).
    robot (Object) : Instance du robot contrôlé par cet adaptateur.
    x (float) : Position x initiale du robot.
    y (float) : Position y initiale du robot.
    dir (float) : Direction actuelle du robot en radians (initialisée à 0).
    distanceParcouru (float) : Distance totale parcourue par le robot (initialisée à 0).
    largeur (float) : Largeur du robot en mm.
    longueur (float) : Longueur du robot en mm.
    crash (bool) : Indicateur de collision (initialisé à False).
    taille_roue (float) : Diametre des roues du robot en mm (initialisée à 8).
    angle_parcourue (float) : Angle total parcouru par le robot (initialisé à 0).
    d (float) : Largeur entre les roues du robot en mm.
    last_motor_pos (tuple) : Dernière position des moteurs enregistrée.
    """

    def __init__(self, robot, x, y, longueur, largeur, monde=None):
        self.monde = monde
        self.robot = robot
        self.x = x
        self.y = y
        self.dir = 0
        self.distanceParcouru = 0
        self.largeur = largeur
        self.longueur = longueur
        self.crash = False
        self.taille_roue = 8
        self.angle_parcourue = 0
        self.d = largeur
        self.last_motor_pos = robot.get_motor_position()

    def update(self):
        """Met à jour les statistiques du robot, calculant les distances parcourues par les roues et ajustant l'angle et la distance totale parcourue."""
        rg, rd = self.robot.get_motor_position()
        drg, drd = ((rg, rd)[0] - self.last_motor_pos[0], (rg, rd)[1] - self.last_motor_pos[1])
        self.last_motor_pos = self.robot.get_motor_position()
        distanceG = math.radians(drg) * self.robot.WHEEL_DIAMETER / 2.0  # distance parcourue par la roue gauche
        distanceD = math.radians(drd) * self.robot.WHEEL_DIAMETER / 2.0  # distance parcourue par la roue droite
        if distanceG != distanceD:
            if abs(distanceG) > abs(distanceD):
                self.angle_parcourue -= distanceG / (-self.robot.WHEEL_BASE_WIDTH * distanceG / (distanceD - distanceG))
            else:
                self.angle_parcourue += distanceD / (-self.robot.WHEEL_BASE_WIDTH * distanceD / (distanceG - distanceD))
        self.distanceParcouru += (distanceD + distanceG) / 2.0

    def resetMotor(self, port, angle):
        """Réinitialise le moteur spécifié à un certain angle."""
        self.robot.offset_motor_encoder(port, angle)

    def getDistanceParcouru(self):
        """Renvoie la distance totale parcourue par le robot."""
        return self.distanceParcouru

    def setVitesse(self, vg, vd):
        """Définit la vitesse des roues gauche et droite du robot.
        
        Paramètres:
        vg (float) : Vitesse de la roue gauche.
        vd (float) : Vitesse de la roue droite.
        """
        if vg == vd:
            self.robot.set_motor_dps(3, vg)
        else:
            self.robot.set_motor_dps(1, vg)
            self.robot.set_motor_dps(2, vd)

    def capteur_distance(self):
        """Renvoie la distance mesurée par le capteur de distance du robot."""
        return self.robot.get_distance()

    def rec(self):
        """Commence l'enregistrement des images du robot."""
        return self.robot._start_recording()

    def stopRec(self):
        """Arrête l'enregistrement des images du robot."""
        return self.robot._stop_recording()

    def getImage(self):
        """Renvoie une image capturée par le robot."""
        return self.robot.get_image()
