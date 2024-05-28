from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle



from direct.showbase.ShowBase import ShowBase

class MyRobot(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = MyRobot()
app.run()