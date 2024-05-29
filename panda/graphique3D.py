from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor

confVars = """
win-size 1280 720
window-title My Robot
show-frame-rate-meter True
"""

loadPrcFileData("", confVars)

class MyRobot(ShowBase):
    def __init__(self):
        super().__init__()

        # Charger le modèle de l'objet
        self.robot = Actor("model/cars", {"anim1": "model/cars"})
        self.robot.setPos(0, 10, 0)
        self.robot.reparentTo(self.render)

        # Charger le modèle de l'environnement
        env = self.loader.loadModel("model/area")
        env.setPos(0, 0, 0)  # Ajusté pour que l'environnement soit à la position d'origine
        env.reparentTo(self.render)

        # Placer la caméra au-dessus de l'objet principal
        self.camera.setPos(0, -20, 20)  # Ajusté pour observer le robot
        self.camera.lookAt(self.robot)

        self.x = 0
        self.y = 0

        self.taskMgr.add(self.update, "update")

    def update(self, task):
        self.robot.setPos(self.x, self.y, 0)
        self.x += 0.01  
        self.y += 0.01  
        return task.cont  # Continuer l'appel de cette tâche à chaque frame

game = MyRobot()
game.run()
