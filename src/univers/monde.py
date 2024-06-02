from src.univers.obstacle import Obstacle
import threading

class Monde(threading.Thread):
    def __init__(self, ligne, colonne, robot=None):
        """
        Constructeur de la classe Monde.
        
        Arguments:
        ligne : nombre de lignes du monde
        colonne : nombre de colonnes du monde
        robot : instance du robot (facultatif)
        """
        self.ligne = ligne  
        self.colonne = colonne
        self.robot = robot  
        self.obstacles = [] 

    def detecter_collision(self, x, y):
        """
        Renvoie true s'il y a collision entre un point et un des obstacles du monde, false sinon.
        
        Arguments:
        x : coordonnée x du point
        y : coordonnée y du point
        
        Retourne:
        True s'il y a collision, False sinon.
        """
        collision = False
        for obs in self.obstacles:
            if collision_rect(self.robot.rect(x, y), obs.getRect()):
                collision = True

        # Vérification des limites du monde
        conditionLimiteX = x - self.robot.longueur / 2 < 1 or x + self.robot.longueur / 2 > self.colonne - 1
        conditionLimiteY = y - self.robot.largeur / 2 < 2 or y + self.robot.largeur / 2 > self.ligne - 2
        
        return collision or (conditionLimiteX or conditionLimiteY)

    def creation_obstacle(self, x, y, z, longueur, largeur, hauteur):
        """
        Ajoute un obstacle à la liste des obstacles.
        
        Arguments:
        x : coordonnée x de l'obstacle
        y : coordonnée y de l'obstacle
        z : coordonnée z de l'obstacle
        longueur : longueur de l'obstacle
        largeur : largeur de l'obstacle
        hauteur : hauteur de l'obstacle
        """
        o1 = Obstacle(x, y, z, longueur, largeur, hauteur)
        self.obstacles.append(o1)

    def place_obstacle(self):
        """Place les obstacles prédéfinis dans le monde."""
        self.creation_obstacle(380, 200, 0, 50, 50, 50)
        self.creation_obstacle(200, 380, 0, 50, 50, 50)
        self.creation_obstacle(150, 150, 0, 50, 50, 50)
        self.creation_obstacle(10, 30, 0, 50, 50, 50)
        self.creation_obstacle(400, 450, 0, 50, 50, 50)
        self.creation_obstacle(480, 249, 0, 50, 50, 50)
        self.creation_obstacle(402, 50, 0, 50, 50, 50)
        self.creation_obstacle(20, 300, 0, 50, 50, 50)
        self.creation_obstacle(15, 460, 0, 50, 50, 50)

    def place_mur(self):
        """Place les murs prédéfinis dans le monde."""
        self.creation_obstacle(250, 1, 0, 1, 500, 1)  # Mur du bas
        self.creation_obstacle(1, 250, 0, 500, 1, 1)  # Mur de gauche
        self.creation_obstacle(250, 499, 0, 1, 500, 1)  # Mur du haut
        self.creation_obstacle(500, 250, 0, 500, 1, 1)  # Mur de droite

    def creation_monde(r1):
        """
        Création d'un monde par défaut.
        
        Arguments:
        r1 : instance du robot
        
        Retourne:
        Une instance de Monde avec le robot fourni.
        """
        monde = Monde(500, 500, r1)
        return monde

    def update(self):
        """Met à jour l'environnement."""
        for obs in self.obstacles:
            if collision_rect(self.robot.getRect(), obs.getRect()):
                self.robot.crash = True
                self.robot.vg = 0
                self.robot.vd = 0
                print("\nLe robot a crashé\n")
                break
        
        self.robot.update()

def collision_rect(r1, r2):
    """
    Renvoie True lorsque les deux rectangles r1 et r2 se superposent.
    
    Arguments:
    r1 : coordonnées et dimensions du premier rectangle
    r2 : coordonnées et dimensions du deuxième rectangle
    
    Retourne:
    True si les rectangles se superposent, False sinon.
    """
    # Déballage des tuples pour obtenir les coordonnées et dimensions des rectangles
    x1, y1, w1, h1 = r1[0][0], r1[0][1], r1[1][0] - r1[0][0], r1[2][1] - r1[0][1]
    x2, y2, w2, h2 = r2[0][0], r2[0][1], r2[1][0] - r2[0][0], r2[2][1] - r2[0][1]
    
    # Vérification de la superposition des rectangles
    return not (x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2)

def collision2(r1, r2):
    """
    Fonction de collision alternative (incomplète et non utilisée).
    
    Arguments:
    r1 : coordonnées et dimensions du premier rectangle
    r2 : coordonnées et dimensions du deuxième rectangle
    
    Retourne:
    La première coordonnée du rectangle r1 (incomplet).
    """
    p1, p2, p3, p4 = r1[0][0], r1[0][1], r1[0][2], r1[0][3]
    o1, o2, o3, o4 = r2[0][0], r2[0][1], r2[0][2], r2[0][3]
    return p1
