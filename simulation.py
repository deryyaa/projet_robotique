from futurama.dexter.robot import Robot
from futurama.univers.monde import Monde
from futurama.univers.obstacle import Obstacle
import math
import time

# Création du monde
monde = Monde(500, 500)

# Création du robot dans le monde
robot = Robot(300, 200, 20, 15 , 10)  # Position du robot dans le monde

#création de 2 obstacle 
for i in range(2):
    monde.setObstacle(Obstacle(2+(i+1)*100, 40, 50, 50)) #creation de plusieurs obstacle pour crée une colision

monde.avancer_robot(10,robot)
        