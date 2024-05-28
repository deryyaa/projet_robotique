
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle
import math


from direct.showbase.ShowBase import ShowBase

class MyRobot(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = MyApp()
app.run()