import tkinter as tk
from Monde import Monde
from Robot import Robot
from time import sleep
import math

window = tk.Tk()
#window.geometry("500x500")
cnv = tk.Canvas(window, width=600, height=400,bg='ivory')
cnv.pack(padx=50, pady=50) #marge en y et x
robot1 = Robot(300, 200,150,100,0,45) # creation d'un robot en point x, y
monde = Monde(600,400)
robot1.avancer(2,monde)

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



def avance(robot,monde,cnv):
    print()
    robot.avancer(10,monde)
    dessineRobot(cnv,robot1)

def a(event):
    avance(robot1,monde,cnv)

window.bind("<Button-1>", a)




window.mainloop()
