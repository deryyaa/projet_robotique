from src.dexter.robot import Robot
from src.univers.obstacle import Obstacle


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
        new_x =robot.x + dx
        new_y = robot.y + dy
        if 0 < new_x-robot.longueur/2 and new_x+robot.longueur/2 < self.ligne and 0 < new_y-robot.largeur/2 and new_y+(robot.largeur)/2 < self.colonne:  
            return True
        return False

    def avancer_robot(self,dt,robot):
        """ verifie si il n'y a pas d'obstacle sur la position dans lequel le robot va avancer"""
        tmpx=robot.x #initialise ces positions dans une variable temporaires
        tmpy=robot.y
        robot.move(dt,self)
        for i in self.obstacles:
            if collision_rect([(i.x-i.longeur/2,i.y-i.largeur/2),(i.x+i.longeur/2,i.y+i.largeur/2)],[(robot.x-robot.longueur/2,robot.y-robot.largeur/2),(robot.x+robot.longueur/2,robot.y+robot.largeur/2)]):
                #si il y a un obstacle on remet le robot a ces positions temporaire d'avant (on le vérifie grâce aux coordonnées)
                robot.x=tmpx
                robot.y=tmpy
                print("le robot vient de percuter le mur")
                break 
                
    def detecter_collision(self,x,y):
        """Renvoie true s'il y a collision entre un point et un des obstacles du monde, false sinon"""
        for obst in self.obstacles:
            # Verifie si collision entre point et obstacle
            if (x >= obst.x and x <= obst.x + obst.longueur and
            y >= obst.y and y <= obst.y + obst.largeur): 
                return True
        return False


def collision_rect(r1, r2):
    """Vérifie si deux rectangles se superposent

    Return True si les rectangles se superposent, False sinon.
    """
    # Prend en parametre une liste de tuple des 2 coordonnées des rectangles (obstacle et robot)
    # Déballage des tuples pour obtenir les coordonnées et dimensions des rectangles
    x1, y1, w1, h1 = r1[0][0], r1[0][1], r1[1][0] - r1[0][0], r1[1][1] - r1[0][1]
    x2, y2, w2, h2 = r2[0][0], r2[0][1], r2[1][0] - r2[0][0], r2[1][1] - r2[0][1]
    
    # Vérification de la superposition des rectangles
    # La superposition est vérifiée en négatif, donc si l'une des conditions est vraie, la superposition n'a pas lieu.
    return not (x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2)
