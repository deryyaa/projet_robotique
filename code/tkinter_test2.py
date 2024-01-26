from tkinter import *
from Robot import Robot

fenetre = Tk()
cnv = Canvas(fenetre, width=600, height=400, bg="ivory")
cnv.create_line(100, 100, 100, 300, width=1, fill="black")
cnv.create_line(100, 300, 500, 300, width=1, fill="black")
cnv.create_line(500, 300, 500, 100, width=1, fill="black")
cnv.create_line(500, 100, 100, 100, width=1, fill="black")

robot1 = Robot(300, 200, 20, 20)

robot_id = cnv.create_rectangle(robot1.x, robot1.y, robot1.x + robot1.largeur, robot1.y + robot1.longueur, fill="blue")

cnv.pack()

def move(event):
    global robot1
    key = event.keysym
    if key == 'Up':
        robot1.avancer(5)
    elif key == 'Down':
        robot1.reculer(5)
    elif key == 'Left':
        robot1.tourner_gauche(10)
    elif key == 'Right':
        robot1.tourner_droite(10)

    cnv.coords(robot_id, robot1.x, robot1.y, robot1.x + robot1.largeur, robot1.y + robot1.longueur)

fenetre.bind('<KeyPress>', move)

fenetre.mainloop()
