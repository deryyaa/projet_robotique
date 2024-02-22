from tkinter import *
from src.dexter.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
from src.univers.controleur import Controleur

import math
import time

class Graphique:
    def __init__(self,monde, FPS=100):
        self.monde=monde
        self.FPS=FPS
    def dessineRobot(self,canvas):
        """Dessine un robot sur le canvas avec les coordonnées et la direction spécifiées
        canvas: Le canvas sur lequel le robot doit être dessiné
        robot: L'objet représentant le robot avec les attributs x, y, dir, largeur et longueur.
        """
        robot=self.monde.robot
        canvas.delete("rectangle")
        cos_robot=math.cos(robot.dir)
        sin_robot=math.sin(robot.dir)
        canvas.create_polygon(robot.x+robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                            robot.x-robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                            robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            fill="blue",tags="rectangle")
        canvas.create_line(robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                            self.monde.colonne-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                            fill="red",tags="rectangle")
    def update(self):
        # Création de la fenêtre principale
        fenetre = Tk()
        fenetre.title("Robot dans le monde")
        # Création du canevas avec les bonnes dimensions en fonction du monde
        cnv = Canvas(fenetre, width=self.monde.ligne+20, height=self.monde.colonne, bg="ivory")
        cnv.pack()
        

# Création du robot dans le mondez
robot1 = Robot(300, 200, 50, 30 , 50)  # Position du robot dans le monde

#création de 2 obstacle 
for i in range(2):
    monde.setObstacle(Obstacle(2+(i+1)*100, 40, 50, 50)) #creation de plusieurs obstacle pour crée une colision
for i in monde.obstacles:
    print(i.x,i.y)
    cnv.create_rectangle(i.x-i.longueur/2,i.y-i.largeur/2,i.x+i.longueur/2,i.y+i.largeur/2,fill="grey") #affichage des 2 obstacles


# Dessin du robot sur le canevas
def dessineRobot(canvas,robot):
    """Dessine un robot sur le canvas avec les coordonnées et la direction spécifiées
    canvas: Le canvas sur lequel le robot doit être dessiné
    robot: L'objet représentant le robot avec les attributs x, y, dir, largeur et longueur.
    """
    canvas.delete("rectangle")
    cos_robot=math.cos(robot.dir)
    sin_robot=math.sin(robot.dir)
    canvas.create_polygon(robot.x+robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                          DIMY-robot.y+robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                          robot.x-robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                          DIMY-robot.y-robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                          robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          DIMY-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          DIMY-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          fill="blue",tags="rectangle")
    canvas.create_line(robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          DIMY-robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          DIMY-robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          fill="red",tags="rectangle")
dessineRobot(cnv,robot1)


def set_time():
    """Définit le temps global utilisé pour le mouvement du robot"""
    global temps
    temps = int(entre1.get())

texte1= Label(fenetre,text="Entrez un temps(secondes)",background="white")
texte1.place(x=10,y=500)

entre1 = Entry(fenetre,background="white")
entre1.place(x=10,y=520)

def set_speed_gauche():
    """Définit la vitesse de la roue gauche du robot"""
    robot1.vg=float(entre2.get())

texte2= Label(fenetre,text="Entrez une vitesse gauche",background="white")
texte2.place(x=10,y=550)

entre2 = Entry(fenetre,background="white")
entre2.place(x=10,y=570)

def set_speed_droite():
    """Définit la vitesse de la roue droite du robot"""
    robot1.vd=float(entre3.get())

texte3= Label(fenetre,text="Entrez une vitesse droite",background="white")
texte3.place(x=10,y=600)
   
entre3 = Entry(fenetre,background="white")
entre3.place(x=10,y=620)


def move(event=None):
    """Déplace le robot selon les vitesses définies pendant le temps spécifié"""
    global robot1,temps
    debut = time.time()
    fin_update = time.time()
    while time.time()-debut<temps: 
        # robot1.move(1./FPS)
        # Mise à jour des coordonnées du robot sur le canevas
        debut_update = time.time()
        monde.avancer_robot(fin_update-debut_update)
        dessineRobot(cnv,robot1)
        fenetre.update()
        fin_update = time.time()
        time.sleep(1./FPS)

def run_functions():
    set_time()
    set_speed_gauche()
    set_speed_droite()
    move()


bouton= Button(fenetre,text="start",command=run_functions)
bouton.place(x=10,y=650)


# Création des instances des classes TracerCarre et AvancerToutDroit
# Création des instances des classes TracerCarre et AvancerToutDroit
#avancer_tout_droit = AvancerToutDroit(robot1)  # Créez une instance de AvancerToutDroit en passant le robot1 comme argument
tracer_carre = TracerCarre(robot1, avancer_tout_droit)  # Créez une instance de TracerCarre en passant le robot1 et avancer_tout_droit comme arguments

# Définir les mouvements du robot
angle = 100
distance_avancer = 200

# Tracer un carré
#tracer_carre.tracer_carre(angle)

# Avancer tout droit
avancer_tout_droit.avancer_tout_droit(distance_avancer)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
