from Robot import Robot
from Obstacle import Obstacle

class Monde:
    def __init__(self, ligne, colonne):
        """ constructeur """
        self.ligne = ligne  # initialisation des coordonnées
        self.colonne = colonne
        self.robot = None
        self.obstacles = []
        self.matrice=[[0 for i in range(self.colonne)] for x in range(self.ligne)]

    def affiche(self):
        """fonction qui permet d'afficher le monde dans le terminal"""
        a = "+" + "-" * self.colonne + "+" + "\n"
        verification=False
        for i in range(self.ligne):
            a += "|"
            for j in range(self.colonne):
                if self.robot is not None and int(self.robot.x) == i and int(self.robot.y) == j:
                    a += "X"
                else:
                    for d in self.obstacles:
                        if int(d.x)==i and int(d.y)==j:
                            verification=True
                            a+="0"
                    if verification:
                        verification=False
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

    def avancer_robot(self,distance,robot):
        """ verifie si il n'y a pas d'obstacle sur la position dans lequel le robot va avancer"""
        tmpx=robot.x
        tmpy=robot.y
        robot.avancer(distance,self)
        for i in self.obstacles:
            if int(i.x) ==int(robot.x) and int(i.y)== int(robot.y):  #si il y a un obstacle on remet le robot a ces positions temporaire d'avant 
                robot.x=tmpx
                robot.y=tmpy
                print("il y a un obstacle")
                break
                