from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
import math
from direct.showbase.ShowBaseGlobal import globalClock
from src.univers.monde import Monde
from src.univers.obstacle import *
import sys
import os

confVars = """
win-size 1280 720
window-title My Robot
show-frame-rate-meter True
sync-video 0
"""

loadPrcFileData("", confVars)

class MyRobot(ShowBase):
    def __init__(self, monde):
        super().__init__()

        self.monde = monde
        self.robot = None  # Initialisation de l'acteur robot
        self.x = monde.robot.x
        self.y = monde.robot.y
        self.z = monde.robot.z
        self.direction = monde.robot.dir
        self.speed = monde.robot.vitesse_max

        self.afficheEnvironnement()
        self.afficheRobot()
        self.afficheObstacle()

        self.taskMgr.add(self.update, "update")

    def deplaceRobot(self):
        dt = globalClock.getDt()
        self.x += self.speed * math.cos(self.direction) * dt
        self.y += self.speed * math.sin(self.direction) * dt

        # Mettre à jour la position de l'acteur robot
        if self.robot:
            self.robot.setPos(self.x, self.y, self.z)

    def afficheRobot(self):
        # Charger le modèle de l'objet
        self.robot = Actor("model/robot", {"anim1": "model/robot"})
        self.robot.setPos(self.monde.robot.x, self.monde.robot.y, self.monde.robot.z)
        self.robot.reparentTo(self.render)

    def afficheObstacle(self):
        # Charger le modèle de l'obstacle
        for obstacle in self.monde.obstacles:
            obs = self.loader.loadModel("model/obstacle")
            obs.setPos(obstacle.x, obstacle.y, obstacle.z)
            obs.reparentTo(self.render)

    def afficheEnvironnement(self):
        # Charger le modèle de l'environnement
        env = self.loader.loadModel("model/area")
        env.setPos(0, 0, 0)
        env.reparentTo(self.render)

    def update(self, task):
        self.deplaceRobot()
        return task.cont  # Continuer l'appel de cette tâche à chaque frame
