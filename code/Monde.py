from Robot import Robot
from Obstacle import Obstacle

class Monde:
    def __init__(self, ligne, colonne):
        """ constructeur """
        self.ligne = ligne  # initialisation des coordonnées
        self.colonne = colonne
        self.robot = None
        self.obstacles = []

    def affiche(self):
        """fonction qui permet d'afficher le monde dans le terminal"""
        a = "+" + "-" * self.colonne + "+" + "\n"
        for i in range(self.ligne):
            a += "|"
            for j in range(self.colonne):
                if self.robot is not None and int(self.robot.x) == i and int(self.robot.y) == j:
                    a += "X"
                else:
                    a += " "
            a += "|\n"

        a += "+" + "-" * self.colonne + "+" + "\n"
        print(a)

    def setRobot(self, robot):
        """Initialise le robot dans le monde"""
        self.robot = robot

    def setObstacle(self, obstacle):
        """Initialise un obstacle dans le monde"""
        self.obstacles.append(obstacle)