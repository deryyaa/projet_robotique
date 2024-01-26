from tkinter import *
from Robot import Robot
from Monde import Monde  # Assurez-vous que la classe Monde est correctement définie dans un fichier Monde.py

# Création du monde
monde = Monde(400, 600)  # Définissez les dimensions du monde

fenetre = Tk()
cnv = Canvas(fenetre, width=monde.colonne, height=monde.ligne, bg="ivory")
cnv.pack()

# Création des limites du monde
cnv.create_line(100, 100, 100, 300, width=1, fill="black")
cnv.create_line(100, 300, 500, 300, width=1, fill="black")
cnv.create_line(500, 300, 500, 100, width=1, fill="black")
cnv.create_line(500, 100, 100, 100, width=1, fill="black")

# Création du robot dans le monde
robot1 = Robot(300, 200, 20, 20, monde)

# Dessin du robot sur le canevas
robot_id = cnv.create_rectangle(robot1.x, robot1.y, robot1.x + robot1.largeur, robot1.y + robot1.longueur, fill="blue")

def move(event):
    key = event.keysym
    if key == 'Up':
        robot1.avancer(5,monde)
    elif key == 'Down':
        robot1.reculer(5,monde)
    elif key == 'Left':
        robot1.tourner_gauche(10)
    elif key == 'Right':
        robot1.tourner_droite(10)

    # Vérifie si les nouvelles coordonnées du robot sont dans les limites du monde
    if 0 <= robot1.x <= monde.colonne - robot1.largeur and 0 <= robot1.y <= monde.ligne - robot1.longueur:
        cnv.coords(robot_id, robot1.x, robot1.y, robot1.x + robot1.largeur, robot1.y + robot1.longueur)

fenetre.bind('<KeyPress>', move)
fenetre.mainloop()


