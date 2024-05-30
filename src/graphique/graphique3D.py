from panda3d.core import loadPrcFileData, Point3
from direct.showbase.ShowBase import ShowBase
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

        self.camDist = 100  # Distance of the camera from the robot
        self.camAngle = 0  # Angle for rotating the camera around the robot

        self.afficheEnvironnement()
        self.afficheRobot()
        self.afficheObstacle()

        self.taskMgr.add(self.update, "update")

        # Enable mouse control for camera
        self.disableMouse()
        self.accept("mouse3", self.startCameraControl)
        self.accept("mouse3-up", self.stopCameraControl)
        self.cameraControl = False

    def startCameraControl(self):
        self.cameraControl = True
        self.mouseX = self.mouseWatcherNode.getMouseX()
        self.mouseY = self.mouseWatcherNode.getMouseY()

    def stopCameraControl(self):
        self.cameraControl = False

    def deplaceRobot(self):
        dt = globalClock.getDt()
        self.x += self.speed * math.cos(self.direction) * dt
        self.y += self.speed * math.sin(self.direction) * dt

        # Mettre à jour la position de l'acteur robot
        if self.robot:
            self.robot.setPos(self.x, self.y, self.z)

    def afficheRobot(self):
        # Charger le modèle de l'objet
        self.robot = self.loader.loadModel("src/graphique/model/robot")
        self.robot.setPos(self.monde.robot.x, self.monde.robot.y, self.monde.robot.z)
        self.robot.setScale(self.monde.robot.longueur / 20.0, self.monde.robot.largeur / 20.0, self.monde.robot.hauteur / 20.0)  # Ajuster la taille du robot
        self.robot.reparentTo(self.render)

    def afficheObstacle(self):
        # Charger le modèle de l'obstacle
        for obstacle in self.monde.obstacles:
            obs = self.loader.loadModel("src/graphique/model/obstacle")
            obs.setScale(obstacle.longueur / 20.0, obstacle.largeur / 20.0, obstacle.hauteur / 20.0)  # Ajuster la taille des obstacles
            obs.setPos(obstacle.x, obstacle.y, obstacle.z)
            obs.reparentTo(self.render)

    def afficheEnvironnement(self):
        # Charger le modèle de l'environnement
        env = self.loader.loadModel("src/graphique/model/area")
        env.setScale(self.monde.colonne, self.monde.ligne, 0)  # Ajuster la taille des obstacles    
        env.setPos(0, 0, 0)
        env.reparentTo(self.render)

    def update(self, task):
        self.deplaceRobot()

        # Update camera rotation
        if self.cameraControl and self.mouseWatcherNode.hasMouse():
            newMouseX = self.mouseWatcherNode.getMouseX()
            newMouseY = self.mouseWatcherNode.getMouseY()

            deltaX = newMouseX - self.mouseX
            deltaY = newMouseY - self.mouseY

            self.camAngle += deltaX * 100  # Adjust sensitivity as needed
            self.camDist -= deltaY * 100
            self.camDist = max(20, self.camDist)  # Prevent the camera from getting too close

            self.mouseX = newMouseX
            self.mouseY = newMouseY

        # Update the camera position to follow the robot
        camX = self.x + self.camDist * math.sin(math.radians(self.camAngle))
        camY = self.y - self.camDist * math.cos(math.radians(self.camAngle))
        self.camera.setPos(camX, camY, self.z + 50)
        self.camera.lookAt(Point3(self.x, self.y, self.z))

        return task.cont  # Continuer l'appel de cette tâche à chaque frame
