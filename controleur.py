from futurama.dexter.robot import Robot
from futurama.univers.monde import Monde

monde = Monde(400, 400)

class Controleur:
    def __init__(self, robot, monde):
        self.robot = robot

    def avancer(self, distance):
        """Commande au robot d'avancer d'une certaine distance"""
        self.robot.avancer_(distance, monde)

    def reculer(self, distance):
        """Commande au robot de reculer d'une certaine distance"""
        self.robot.reculer_(distance, monde)

    def augmenter_vitesse_gauche(self, n):
        """Augmente la vitesse de la roue gauche"""
        self.robot.augmenter_vg(n)

    def augmenter_vitesse_droite(self, n):
        """Augmente la vitesse de la roue droite"""
        self.robot.augmenter_vd(n)

    def deplacer(self, distance, temps):
        """Déplace le robot avec une distance pendant un temps spécifié"""
        self.robot.vitesse_discrete(distance, temps, monde)
        
    def carre(self):
        """Se deplace en forme de carré"""
        for i in range(4):
            self.robot.vg=self.robot.vitesse_max
            self.robot.vd=self.robot.vitesse_max
            for i in range(10):
                self.robot.mouvement(0.1)
            self.robot.vg=15
            self.robot.vd=-15
            for i in range(30):
                self.robot.mouvement(0.1)
            