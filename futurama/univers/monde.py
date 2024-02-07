from futurama.dexter.robot import Robot
from futurama.univers.obstacle import Obstacle
from utilitaire import collision_rect

class Monde:
    def __init__(self, ligne, colonne):
        """ constructeur """
        self.ligne = ligne  # initialisation des coordonnées
        self.colonne = colonne
        self.robot = None
        self.obstacles = [] #création de la liste d'obstacle
    
    def setRobot(self, robot):
        """Initialise le robot dans le monde"""
        self.robot = robot 

    def setObstacle(self, obstacle):
        """Initialise un obstacle dans le monde"""
        self.obstacles.append(obstacle)

    def peut_avancer(self, dx, dy, robot):
        """ Vérifie si le robot peut avancer sans dépasser les limites du monde """
        new_x = robot.x + dx
        new_y = robot.y + dy
        if 0 <= new_x-robot.longueur/2 and new_x-robot.longueur/2 < self.ligne and 0 <= new_y-robot.longueur/2 and new_y+(robot.longueur)/2 < self.colonne:  
            return True
        return False

    def avancer_robot(self,distance,robot):
        """ verifie si il n'y a pas d'obstacle sur la position dans lequel le robot va avancer"""
        tmpx=robot.x #initialise ces positions dans une variable temporaires
        tmpy=robot.y
        robot.avancer(distance,self)
        for i in self.obstacles:
            if collision_rect([(i.x-i.longeur/2,i.y-i.largeur/2),(i.x+i.longeur/2,i.y+i.largeur/2)],[(robot.x-robot.longueur/2,robot.y-robot.largeur/2),(robot.x+robot.longueur/2,robot.y+robot.largeur/2)]):
                #si il y a un obstacle on remet le robot a ces positions temporaire d'avant (on le vérifie grâce aux coordonnées)
                robot.x=tmpx
                robot.y=tmpy
                print("le robot vient de percuter le mur")
                break 
                
    
    
  