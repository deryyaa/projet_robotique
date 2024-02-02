from robot import Robot
from obstacle import Obstacle

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
            if Monde.collision_rect([(i.x-i.longeur/2,i.y-i.largeur/2),(i.x+i.longeur/2,i.y+i.largeur/2)],[(robot.x-robot.longueur/2,robot.y-robot.largeur/2),(robot.x+robot.longueur/2,robot.y+robot.largeur/2)]):
                #si il y a un obstacle on remet le robot a ces positions temporaire d'avant 
                robot.x=tmpx
                robot.y=tmpy
                print("il y a un obstacle")
                break
                
        
    
    def collision_rect(r1,r2): #prend en parametre une liste de tuple des 2 coordonnées de mon rectangle (obstacle et robot)
        """renvoie True quand les 2 rectangle r1,r2 se superpose"""
        x1,y1,w1,h1 = r1[0][0], r1[0][1], r1[1][0] - r1[0][0], r1[1][1] - r1[0][1]
        x2,y2,w2,h2= r2[0][0], r2[0][1], r2[1][0] - r2[0][0], r2[1][1] - r2[0][1]

        return [True,False][x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2]

