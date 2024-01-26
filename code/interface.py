import tkinter as tk
from Monde import Monde
from Robot import Robot
window = tk.Tk()
#window.geometry("500x500")
cnv = tk.Canvas(window, width=600, height=400,bg='ivory')
cnv.pack(padx=50, pady=50) #marge en y et x
robot1 = Robot(300, 200,100,150) # creation d'un robot en point x, y
#monde = Monde(10,20)
#robot1.avancer(monde,2, 5)

cnv.create_polygon(robot1.x-(robot1.longueur/2),robot1.y-(robot1.largeur/2),
                    robot1.x+(robot1.longueur/2),robot1.y-(robot1.largeur/2),
                    robot1.x+(robot1.longueur/2),robot1.y+(robot1.largeur/2),
                    robot1.x-(robot1.longueur/2),robot1.y+(robot1.largeur/2),fill="blue")









window.mainloop()
