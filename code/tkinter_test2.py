from tkinter import *
from Robot import Robot
from Monde import Monde

# Création du monde
monde = Monde(400, 400)

# Création de la fenêtre principale
fenetre = Tk()
fenetre.title("Robot dans le monde")

# Création du canevas avec les bonnes dimensions en fonction du monde
cnv = Canvas(fenetre, width=monde.colonne, height=monde.ligne, bg="ivory")
cnv.pack()

# Création du robot dans le monde
robot1 = Robot(300, 200, 20, 20)  # Position du robot dans le monde

# Dessin du robot sur le canevas
robot_id = cnv.create_rectangle(robot1.x, robot1.y, robot1.x + robot1.largeur, robot1.y + robot1.longueur, fill="blue")

def move(event):
    global robot1
    key = event.keysym
    if key == 'Up':
        robot1.avancer(5, monde)  # Utilisation de la méthode avancer avec le monde
    elif key == 'Down':
        robot1.reculer(5, monde)   # Utilisation de la méthode reculer avec le monde
    elif key == 'Left':
        robot1.tourner_gauche(10)
    elif key == 'Right':
        robot1.tourner_droite(10)

    # Mise à jour des coordonnées du robot sur le canevas
    cnv.coords(robot_id, robot1.x, robot1.y, robot1.x + robot1.largeur, robot1.y + robot1.longueur)

# Association de la fonction de mouvement à l'événement de pression de touche
fenetre.bind('<KeyPress>', move)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
