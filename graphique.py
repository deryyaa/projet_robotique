from tkinter import *
from futurama.dexter.robot import Robot
from futurama.univers.monde import Monde
from futurama.univers.obstacle import Obstacle
import math
import time

# Création du monde
monde = Monde(500, 500)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Robot dans le monde")

# Création du canevas avec les bonnes dimensions en fonction du monde
cnv = Canvas(fenetre, width=monde.colonne+20, height=monde.ligne, bg="ivory")
cnv.pack()

# Création du robot dans le monde
robot1 = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde

#création de 2 obstacle 
for i in range(2):
    monde.setObstacle(Obstacle(2+(i+1)*100, 40, 50, 50)) #creation de plusieurs obstacle pour crée une colision
for i in monde.obstacles:
    print(i.x,i.y)
    cnv.create_rectangle(i.x-i.longeur/2,i.y-i.largeur/2,i.x+i.longeur/2,i.y+i.largeur/2,fill="grey") #affichage des 2 obstacles


# Dessin du robot sur le canevas
def dessineRobot(canvas,robot):
    """Dessine un robot sur le canvas avec les coordonnées et la direction spécifiées
    canvas: Le canvas sur lequel le robot doit être dessiné
    robot: L'objet représentant le robot avec les attributs x, y, dir, largeur et longueur.
    """
    canvas.delete("rectangle")
    cos_robot=math.cos(math.radians(robot.dir))
    sin_robot=math.sin(math.radians(robot.dir))
    canvas.create_polygon(robot.x+robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                          robot.y+robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                          robot.x-robot.largeur/2*sin_robot-robot.longueur/2*cos_robot,
                          robot.y-robot.largeur/2*cos_robot+robot.longueur/2*sin_robot,
                          robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          fill="blue",tags="rectangle")
    canvas.create_line(robot.x-robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          robot.y-robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
                          robot.x+robot.largeur/2*sin_robot+robot.longueur/2*cos_robot,
                          robot.y+robot.largeur/2*cos_robot-robot.longueur/2*sin_robot,
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
    robot1.vg=int(entre2.get())

texte2= Label(fenetre,text="Entrez une vitesse gauche",background="white")
texte2.place(x=10,y=550)

entre2 = Entry(fenetre,background="white")
entre2.place(x=10,y=570)

def set_speed_droite(v):
    """Définit la vitesse de la roue droite du robot"""
    robot1.vd=int(v)

texte2= Label(fenetre,text="Entrez une vitesse droite",background="white")
texte2.place(x=10,y=600)
   
entre3 = Entry(fenetre,background="white")
entre3.place(x=10,y=620)


def move(event=None):
    """Déplace le robot selon les vitesses définies pendant le temps spécifié"""
    global robot1,monde,vitesse,temps
    a=0
    if a == 1:
        for i in range(4):
            robot1.vg=robot1.vitesse_max
            robot1.vd=robot1.vitesse_max
            for i in range(10):
                robot1.mouvement(0.1)
                dessineRobot(cnv,robot1)
                fenetre.update()
                time.sleep(0.1)
            robot1.vg=15
            robot1.vd=-15
            for i in range(30):
                robot1.mouvement(0.1)
                dessineRobot(cnv,robot1)
                fenetre.update()
                time.sleep(0.1)
    debut = time.time()
    while time.time()-debut<temps: 
        robot1.mouvement(0.1)
        # Mise à jour des coordonnées du robot sur le canevas
        dessineRobot(cnv,robot1)
        fenetre.update()
        time.sleep(0.1)

fenetre.bind('<KeyPress>', move)
bouton= Button(fenetre,text="start",command=move)
bouton.pack(padx=50,pady=50)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
