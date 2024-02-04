from tkinter import *
from robot.robot import Robot
from univers.monde import Monde
from univers.obstacle import Obstacle
import math

# Création du monde
monde = Monde(400, 400)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Robot dans le monde")

# Création du canevas avec les bonnes dimensions en fonction du monde
cnv = Canvas(fenetre, width=monde.colonne+20, height=monde.ligne, bg="ivory")
cnv.pack()

# Création du robot dans le monde
robot1 = Robot(300, 200, 20, 20)  # Position du robot dans le monde

#création de 2 obstacle 
for i in range(2):
    monde.setObstacle(Obstacle(2+(i+1)*100, 40, 50, 50)) #creation de plusieurs obstacle pour crée une colision
for i in monde.obstacles:
    print(i.x,i.y)
    cnv.create_rectangle(i.x-i.longeur/2,i.y-i.largeur/2,i.x+i.longeur/2,i.y+i.largeur/2,fill="grey") #affichage des 2 obstacles



# Dessin du robot sur le canevas
def dessineRobot(canvas,robot):
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
dessineRobot(cnv,robot1)


vitesse = 5

def speed(event):
    global vitesse
    key = event.keysym
    if key == "p":
        if vitesse <30:
            vitesse += 5
    elif key == "m" and vitesse - 5 > 0:
        vitesse -= 5  
    return vitesse

def move(event):
    global robot1,monde,vitesse
    key = event.keysym
    pas=speed(event)
    if key == 'Up':
        #robot1.avancer(5, monde)  # Utilisation de la méthode avancer avec le monde
        monde.avancer_robot(pas,robot1)
    elif key == 'Down':
        #robot1.avancer(-5, monde)   # Utilisation de la méthode reculer avec le monde
        monde.avancer_robot(-pas,robot1)
    elif key == 'Left':
        robot1.tourner_droite(10)
    elif key == 'Right':
        robot1.tourner_gauche(10)

    # Mise à jour des coordonnées du robot sur le canevas
    dessineRobot(cnv,robot1)



# Association de la fonction de mouvement à l'événement de pression de touche
fenetre.bind('<KeyPress>', move)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
