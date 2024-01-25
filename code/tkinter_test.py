from tkinter import *
from Robot import Robot
fenetre =Tk()
cnv=Canvas(fenetre,width=600,height=400,bg="ivory")
cnv.create_line(100,100,100,300,width=1,fill="black")
cnv.create_line(100,300,500,300,width=1,fill="black")
cnv.create_line(500,300,500,100,width=1,fill="black")
cnv.create_line(500,100,100,100,width=1,fill="black")

robot1 = Robot(0, 0)


cnv.pack()
fenetre.mainloop()