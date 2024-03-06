from src.univers.obstacle import Obstacle
import threading

class Monde(threading.Thread):
    def __init__(self, ligne, colonne, robot=None):
        """ constructeur """
        self.ligne = ligne  # initialisation des coordonnées
        self.colonne = colonne
        self.robot = robot
        self.obstacles = [] #création de la liste d'obstacle

    def detecter_collision(self,x,y):
        """Renvoie true s'il y a collision entre un point et un des obstacles du monde, false sinon"""
        for obst in self.obstacles:
            conditionX=x-self.robot.longueur/2 >= (obst.x- obst.longueur/2) and self.robot.longueur/2+x <= (obst.x + obst.longueur/2)
            conditionY=y-self.robot.largeur/2 >= (obst.y-obst.largeur/2) and y+self.robot.largeur/2 <= (obst.y + obst.largeur/2)
            conditionLimiteX = x-self.robot.longueur/2 < 1 or x + self.robot.longueur/2 > self.colonne-1
            conditionLimiteY = y - self.robot.largeur/2 < 2 or y+ self.robot.largeur/2 > self.ligne-2
            # Verifie si collision entre point et obstacle
            if (conditionX and conditionY) or (conditionLimiteX or conditionLimiteY):
                return True
            return False
    
    def creation_obstacle(self,x,y,longeur,largeur):
        """rajoute un obstacle a la liste"""
        o1=Obstacle(x,y,longeur,largeur)
        self.obstacles.append(o1)
        
    def place_obstacle(self):
        """Place les obstacles dans le monde"""
        self.creation_obstacle(380,200,50,50) #obstacle
        self.creation_obstacle(250,1,1,500) # mur du bas 
        self.creation_obstacle(1,250,500,1) # mur du gauche
        self.creation_obstacle(250,499,1,500) # mur du haut
        self.creation_obstacle(500,250,500,1) # mur du droit 

    def creation_monde(r1) :
        """Creation d'un monde"""
        monde = Monde(500, 500, r1)
        return monde

        
    def update(self):
        for obs in self.obstacles:
            if collision_rect(self.robot.getRect(),obs.getRect()):
                self.robot.crash=True
                self.robot.vg=0
                self.robot.vd=0
                print("crash")
        self.robot.move(0.01)


def collision_rect(r1,r2): #prend en parametre une liste de tuple des 2 coordonnées de mon rectangle (obstacle et robot)
    """renvoie True quand les 2 rectangle r1,r2 se superpose"""
    # Déballage des tuples pour obtenir les coordonnées et dimensions des rectangles
    x1,y1,w1,h1 = r1[0][0], r1[0][1], r1[1][0] - r1[0][0], r1[2][1] - r1[0][1]
    x2,y2,w2,h2= r2[0][0], r2[0][1], r2[1][0] - r2[0][0], r2[2][1] - r2[0][1]
    # Vérification de la superposition des rectangles
    # La superposition est vérifiée en négatif, donc si l'une des conditions est vraie, la superposition n'a pas lieu.
    return not(x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2)

