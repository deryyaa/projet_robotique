import tkinter as tk
from Monde import Monde
from Robot import Robot
from time import sleep
window = tk.Tk()
#window.geometry("500x500")
cnv = tk.Canvas(window, width=600, height=400,bg='ivory')
cnv.pack(padx=50, pady=50) #marge en y et x
robot1 = Robot(300, 200,100,150) # creation d'un robot en point x, y
monde = Monde(600,400)
robot1.avancer(monde,2, 5)

robot1.polygone=cnv.create_polygon(robot1.x-(robot1.longueur/2),robot1.y-(robot1.largeur/2),
                    robot1.x+(robot1.longueur/2),robot1.y-(robot1.largeur/2),
                    robot1.x+(robot1.longueur/2),robot1.y+(robot1.largeur/2),
                    robot1.x-(robot1.longueur/2),robot1.y+(robot1.largeur/2),fill="blue")

def avance(robot,monde,cnv):
    print()
    robot.avancer(monde,10, 0)
    cnv.delete(robot.polygone)
    robot.polygone=cnv.create_polygon(robot.x-(robot.longueur/2),robot.y-(robot.largeur/2),
                    robot.x+(robot.longueur/2),robot.y-(robot.largeur/2),
                    robot.x+(robot.longueur/2),robot.y+(robot.largeur/2),
                    robot.x-(robot.longueur/2),robot.y+(robot.largeur/2),fill="blue")


def a(event):
    avance(robot1,monde,cnv)

window.bind("<Button-1>", a)




window.mainloop()
