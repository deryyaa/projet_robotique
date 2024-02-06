import unittest
from ..robot.robot import Robot
from ..univers.monde import Monde

# TEST CLASSE ROBOT
print("test robot")
# creation des robots
robot = Robot(0, 0,0,0) # creation d'un robot en point x, y

monde = Monde(10,20) # creation d'un monde x*y

# affichage des positions initiales
print("robot :", robot.x, robot.y)

monde.affiche()
monde.setRobot(robot)
robot.deplacement_vitesse(5,10,monde)
monde.affiche()