from panda3d.core import loadPrcFileData, Point3, TextNode
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.showbase.DirectObject import DirectObject
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

class MyRobot(ShowBase, DirectObject):
    def __init__(self, monde, strategie):
        super().__init__()

        self.monde = monde
        self.robot = None  # Initialisation de l'acteur robot
        self.x = monde.robot.x
        self.y = monde.robot.y
        self.z = monde.robot.z
        self.direction = monde.robot.dir
        self.speed = monde.robot.vitesse_max
        self.strategie = strategie

        self.camDist = 1000  # Distance of the camera from the robot
        self.camAngle = 0  # Horizontal angle for rotating the camera around the robot
        self.camPitch = 10  # Vertical angle for rotating the camera around the robot (set to -45 to look from above)
        self.camHeight = 50  # Height of the camera above the robot

        self.afficheEnvironnement()
        self.afficheRobot()
        self.afficheObstacle()

        self.taskMgr.add(self.update3D, "update")

        # Enable mouse control for camera
        self.disableMouse()
        self.accept("mouse3", self.startCameraControl)
        self.accept("mouse3-up", self.stopCameraControl)
        self.accept("wheel_up", self.zoomIn)
        self.accept("wheel_down", self.zoomOut)
        self.cameraControl = False

        # Set initial camera position
        self.setInitialCameraPosition()

        # Setup text for displaying robot coordinates
        self.setupText()

    def startCameraControl(self):
        self.cameraControl = True
        self.mouseX = self.mouseWatcherNode.getMouseX()
        self.mouseY = self.mouseWatcherNode.getMouseY()

    def stopCameraControl(self):
        self.cameraControl = False

    def deplaceRobot(self):
        self.x = self.robot.x
        self.y = self.robot.y
        
    def zoomIn(self):
        self.camDist = max(20, self.camDist - 50)

    def zoomOut(self):
        self.camDist += 50

    def deplaceRobot(self):
        dt = globalClock.getDt()  # Obtient l'intervalle de temps écoulé depuis la dernière frame
        self.monde.robot.update()  # Met à jour la position et la direction du robot

        # Mise à jour de la position du modèle graphique du robot
        self.robot.setPos(self.monde.robot.x, self.monde.robot.y, self.monde.robot.z)
        self.robot.setH(math.degrees(self.monde.robot.dir))

        # Envoyer un signal pour mettre à jour les coordonnées
        self.messenger.send("update_coordinates", [self.monde.robot.x, self.monde.robot.y])

    def rotationRobot(self):
        self.robot.setH(self.robot,((self.monde.robot.dir)*180)/(math.pi))

    def afficheRobot(self):
        # Charger le modèle de l'objet
        self.robot = self.loader.loadModel("src/graphique/model/robot")
        self.robot.setPos(self.monde.robot.x, self.monde.robot.y, self.monde.robot.z)
        self.robot.setH(self.robot,(self.monde.robot.dir * 180) / math.pi)
        self.robot.reparentTo(self.render)

    def afficheObstacle(self):
        # Charger le modèle de l'obstacle
        for obstacle in self.monde.obstacles:
            obs = self.loader.loadModel("src/graphique/model/obstacle")
            obs.setPos(obstacle.x, obstacle.y, obstacle.z)
            obs.reparentTo(self.render)

    def afficheEnvironnement(self):
        # Charger le modèle de l'environnement
        env = self.loader.loadModel("src/graphique/model/area")
        env.reparentTo(self.render)

    def setInitialCameraPosition(self):
        # Calculate the initial camera's position
        camX = self.x + self.camDist * math.cos(math.radians(self.camPitch)) * math.sin(math.radians(self.camAngle))
        camY = self.y + self.camDist * math.cos(math.radians(self.camPitch)) * -math.cos(math.radians(self.camAngle))
        camZ = self.z + self.camDist * math.sin(math.radians(self.camPitch))

        self.camera.setPos(camX, camY, camZ)
        self.camera.lookAt(Point3(self.x, self.y, self.z))

    def update3D(self, task):
        self.deplaceRobot()

        # Update camera rotation
        if self.cameraControl and self.mouseWatcherNode.hasMouse():
            newMouseX = self.mouseWatcherNode.getMouseX()
            newMouseY = self.mouseWatcherNode.getMouseY()

            deltaX = newMouseX - self.mouseX
            deltaY = newMouseY - self.mouseY

            self.camAngle += deltaX * 100  # Adjust sensitivity as needed
            self.camPitch -= deltaY * 100
            self.camPitch = max(-89, min(89, self.camPitch))  # Limit the vertical angle

            self.mouseX = newMouseX
            self.mouseY = newMouseY

        # Calculate the camera's position
        camX = self.x + self.camDist * math.cos(math.radians(self.camPitch)) * math.sin(math.radians(self.camAngle))
        camY = self.y + self.camDist * math.cos(math.radians(self.camPitch)) * -math.cos(math.radians(self.camAngle))
        camZ = self.z + self.camDist * math.sin(math.radians(self.camPitch))

        self.camera.setPos(camX, camY, camZ)
        self.camera.lookAt(Point3(self.x, self.y, self.z))

        return task.cont  # Continuer l'appel de cette tâche à chaque frame

    def setupText(self):
        # Créer un objet OnscreenText pour afficher les coordonnées du robot
        self.coordText = OnscreenText(
            text="",
            pos=(-1.75, 0.95),
            scale=0.07,
            fg=(1, 1, 1, 1),  # Couleur du texte (blanc)
            align=TextNode.ALeft,
            mayChange=True  # Indique que le texte peut changer dynamiquement
        )

        # Mettre à jour le texte des coordonnées à chaque frame
        self.accept("update_coordinates", self.updateCoordinates)

    def updateCoordinates(self, x, y):
        # Mettre à jour le texte avec les nouvelles coordonnées
        self.coordText.setText(f"x = {x:.2f}, y = {y:.2f}")