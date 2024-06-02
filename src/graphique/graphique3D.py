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
    """Classe principale pour la visualisation 3D du robot dans Panda3D."""

    def __init__(self, monde, strategie):
        """Initialise la classe MyRobot."""

        super().__init__()

        self.monde = monde # Attribue un monde à la simulation
        self.robot = None  # Initialisation de l'acteur robot

        self.x = monde.robot.x  # Coordonnée x initiale du robot
        self.y = monde.robot.y  # Coordonnée y initiale du robot
        self.z = monde.robot.z  # Coordonnée z initiale du robot
        self.direction = monde.robot.dir  # Direction initiale du robot

        self.strategie = strategie  # Stratégie associée au robot

        # Paramètres de la caméra
        self.camDist = 1000  # Distance de la caméra par rapport au robot
        self.camAngle = 0  # Angle horizontal pour la rotation de la caméra autour du robot
        self.camPitch = 10  # Angle vertical pour la rotation de la caméra autour du robot (mis à -45 pour une vue de dessus)
        self.camHeight = 50  # Hauteur de la caméra au-dessus du robot

        # Affichage initial de l'environnement, du robot et des obstacles
        self.afficheEnvironnement()  # Affiche l'environnement
        self.afficheRobot()  # Affiche le robot
        self.afficheObstacle()  # Affiche les obstacles

        # Ajoute la méthode update3D à la gestion des tâches pour mettre à jour l'affichage
        self.taskMgr.add(self.update3D, "update")

        # Active le contrôle de la caméra avec la souris
        self.disableMouse()  # Désactive le contrôle de la caméra par défaut avec la souris
        self.accept("mouse3", self.startCameraControl)  # Active le contrôle de la caméra avec le clic droit de la souris
        self.accept("mouse3-up", self.stopCameraControl)  # Désactive le contrôle de la caméra lorsque le clic droit est relâché
        self.accept("wheel_up", self.zoomIn)  # Zoom avant avec la molette de la souris
        self.accept("wheel_down", self.zoomOut)  # Zoom arrière avec la molette de la souris
        self.cameraControl = False  # Initialise le contrôle de la caméra à False

        # Définit la position initiale de la caméra
        self.setInitialCameraPosition()

        # Configure le texte pour afficher les coordonnées du robot
        self.setupText()


    def startCameraControl(self):
        """Démarre le contrôle de la caméra avec les boutons de la souris."""
        
        self.cameraControl = True  # Active le contrôle de la caméra
        # Enregistre la position actuelle de la souris pour suivre les mouvements ultérieurs
        self.mouseX = self.mouseWatcherNode.getMouseX()  
        self.mouseY = self.mouseWatcherNode.getMouseY()
        
    def stopCameraControl(self):
        """Arrête le contrôle de la caméra avec le bouton de la souris."""
        self.cameraControl = False # Désactive le contrôle de la caméra
        
    def zoomIn(self):
        """Rapproche la caméra du robot."""
        # Réduit la distance de la caméra par rapport au robot, sans dépasser la limite minimale de 20
        self.camDist = max(20, self.camDist - 50) 

    def zoomOut(self):
        """Éloigne la caméra du robot."""
        # Augmente la distance de la caméra par rapport au robot
        self.camDist += 50

    def deplaceRobot(self):
        """Met à jour la position du robot dans l'environnement 3D."""
        
        dt = globalClock.getDt()  # Obtient l'intervalle de temps écoulé depuis la dernière frame
        self.monde.robot.update()  # Met à jour la position et la direction du robot

        # Mise à jour de la position du modèle graphique du robot
        self.robot.setPos(self.monde.robot.x, self.monde.robot.y, self.monde.robot.z)
        self.robot.setH(math.degrees(self.monde.robot.dir))

        # Envoyer un signal pour mettre à jour les coordonnées
        self.messenger.send("update_coordinates", [self.monde.robot.x, self.monde.robot.y])

    def afficheRobot(self):
        """Charge et affiche le modèle 3D du robot."""
        # Charger le modèle de l'objet
        self.robot = self.loader.loadModel("src/graphique/model/robot")
        # Positionner le modèle à la position du robot dans le monde
        self.robot.setPos(self.monde.robot.x, self.monde.robot.y, self.monde.robot.z)
        # Définir l'orientation du robot en fonction de sa direction
        self.robot.setH(self.robot, (self.monde.robot.dir * 180) / math.pi)
        # Attacher le modèle du robot au rendu de la scène
        self.robot.reparentTo(self.render)

    def afficheObstacle(self):
        """Charge et affiche le modèle 3D des obstacles."""
        # Parcourir la liste des obstacles dans le monde
        for obstacle in self.monde.obstacles:
            # Charger le modèle de l'obstacle
            obs = self.loader.loadModel("src/graphique/model/obstacle")
            # Positionner l'obstacle à sa position dans le monde
            obs.setPos(obstacle.x, obstacle.y, obstacle.z)
            # Attacher le modèle de l'obstacle au rendu de la scène
            obs.reparentTo(self.render)

    def afficheEnvironnement(self):
        """Charge et affiche le modèle 3D de l'environnement."""
        # Charger le modèle de l'environnement
        env = self.loader.loadModel("src/graphique/model/area")
        # Attacher le modèle de l'environnement au rendu de la scène
        env.reparentTo(self.render)

    def setInitialCameraPosition(self):
        """Configure la position initiale de la caméra."""
       # Calculer la position initiale de la caméra
        camX = self.x + self.camDist * math.cos(math.radians(self.camPitch)) * math.sin(math.radians(self.camAngle))
        camY = self.y + self.camDist * math.cos(math.radians(self.camPitch)) * -math.cos(math.radians(self.camAngle))
        camZ = self.z + self.camDist * math.sin(math.radians(self.camPitch))

        # Définir la position de la caméra
        self.camera.setPos(camX, camY, camZ)
        # Orienter la caméra pour qu'elle regarde vers le point spécifié
        self.camera.lookAt(Point3(self.x, self.y, self.z))

    def update3D(self, task):
        """Met à jour la vue 3D."""
        # Déplacer le robot
        self.deplaceRobot()  # Appelle une fonction pour déplacer le robot dans la scène.

        # Mettre à jour la rotation de la caméra si le contrôle de la caméra est activé et la souris est détectée.
        if self.cameraControl and self.mouseWatcherNode.hasMouse():
            # Obtenir les nouvelles positions de la souris
            newMouseX = self.mouseWatcherNode.getMouseX()
            newMouseY = self.mouseWatcherNode.getMouseY()

            # Calculer le changement dans la position de la souris
            deltaX = newMouseX - self.mouseX
            deltaY = newMouseY - self.mouseY

            # Ajuster l'angle de la caméra en fonction du mouvement de la souris avec une sensibilité donnée.
            self.camAngle += deltaX * 100  # Sensibilité ajustable selon les besoins.
            self.camPitch -= deltaY * 100
            # Limiter l'angle vertical entre -89 et 89 degrés.
            self.camPitch = max(-89, min(89, self.camPitch))

            # Mettre à jour les positions de la souris.
            self.mouseX = newMouseX
            self.mouseY = newMouseY

        # Calculer la position de la caméra en fonction de l'angle de la caméra et de la distance par rapport au point spécifié.
        camX = self.x + self.camDist * math.cos(math.radians(self.camPitch)) * math.sin(math.radians(self.camAngle))
        camY = self.y + self.camDist * math.cos(math.radians(self.camPitch)) * -math.cos(math.radians(self.camAngle))
        camZ = self.z + self.camDist * math.sin(math.radians(self.camPitch))

        # Définir la position de la caméra.
        self.camera.setPos(camX, camY, camZ)
        # Orienter la caméra pour qu'elle regarde vers le point spécifié.
        self.camera.lookAt(Point3(self.x, self.y, self.z))

        return task.cont  # Continuer l'appel de cette tâche à chaque frame.

def setupText(self):
    """Configure l'affichage du texte des coordonnées."""
    # Créer un objet OnscreenText pour afficher les coordonnées du robot.
    self.coordText = OnscreenText(
        text="",  # Texte initial vide.
        pos=(-1.75, 0.95),  # Position de l'affichage du texte à l'écran.
        scale=0.07,  # Échelle du texte.
        fg=(1, 1, 1, 1),  # Couleur du texte (blanc).
        align=TextNode.ALeft,  # Alignement du texte à gauche.
        mayChange=True  # Indique que le texte peut changer dynamiquement.
    )

    # Mettre à jour le texte des coordonnées à chaque frame en écoutant l'événement "update_coordinates".
    self.accept("update_coordinates", self.updateCoordinates)
    
    def updateCoordinates(self, x, y):
        """Met à jour le texte affichant les coordonnées du robot."""
        # Mettre à jour le texte avec les nouvelles coordonnées
        self.coordText.setText(f"x = {x:.2f}, y = {y:.2f}")