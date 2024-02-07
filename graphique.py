from tkinter import *
from futurama.dexter.robot import Robot
from futurama.univers.monde import Monde
from futurama.univers.obstacle import Obstacle
import math
import time

# Création du monde
monde = Monde(400, 400)

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
    canvas.create_polygon(robot.x+robot.longueur/2*cos_robot-robot.largeur/2*sin_robot,
                          robot.y+robot.longueur/2*sin_robot+robot.largeur/2*cos_robot,
                          robot.x-robot.longueur/2*cos_robot-robot.largeur/2*sin_robot,
                          robot.y-robot.longueur/2*sin_robot+robot.largeur/2*cos_robot,
                          robot.x-robot.longueur/2*cos_robot+robot.largeur/2*sin_robot,
                          robot.y-robot.longueur/2*sin_robot-robot.largeur/2*cos_robot,
                          robot.x+robot.longueur/2*cos_robot+robot.largeur/2*sin_robot,
                          robot.y+robot.longueur/2*sin_robot-robot.largeur/2*cos_robot,
                          fill="blue",tags="rectangle")
    canvas.create_line(robot.x+robot.longueur/2*cos_robot-robot.largeur/2*sin_robot,
                          robot.y+robot.longueur/2*sin_robot+robot.largeur/2*cos_robot,
                          robot.x+robot.longueur/2*cos_robot+robot.largeur/2*sin_robot,
                          robot.y+robot.longueur/2*sin_robot-robot.largeur/2*cos_robot,
                          fill="red",tags="rectangle")
dessineRobot(cnv,robot1)


vitesse = 5


temps=1
def set_time(t):
    global temps
    temps = int(t)
curseur1 = Scale(fenetre, orient = "horizontal", label="temps",command=set_time, from_=1, to=100)
curseur1.pack()

vitesse=1
def set_speed(v):
    global vitesse
    vitesse = int(v)
curseur2 = Scale(fenetre, orient = "horizontal", label="vitesse",command=set_speed, from_=1, to=100)
curseur2.pack()

def move(event):
    global robot1,monde,vitesse
    key = event.keysym
    pas=speed(event)
    if key =='p':
        #robot1.avancer(5, monde)  # Utilisation de la méthode avancer avec le monde
        robot1.mouvement(0.05)
    if key == 'Up':
        #robot1.avancer(5, monde)  # Utilisation de la méthode avancer avec le monde
        robot1.avancer()
    elif key == 'Down':
        #robot1.avancer(-5, monde)   # Utilisation de la méthode reculer avec le monde
        robot1.reculer()
    elif key == 'Right':
        robot1.tourner_droite()
    elif key == 'Left':
        robot1.tourner_gauche()
    elif key == 'd' :
        robot1.augmenter_vd(1)
    elif key == 'g' :
        robot1.augmenter_vg(1)
        

    # Mise à jour des coordonnées du robot sur le canevas
    dessineRobot(cnv,robot1)



# Association de la fonction de mouvement à l'événement de pression de touche
fenetre.bind('<KeyPress>', move)
# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
