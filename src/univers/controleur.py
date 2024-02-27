import time
from threading import Thread
class Controleur(Thread):
    def __init__(self,robot,FPS=100):
        self.robot = robot
        self.FPS=FPS

    class AvancerToutDroit():
        def __init__(self, distance,robot,FPS=100):
            self.distance = distance
            self.robot=robot
            self.FPS=FPS
                        
        def start(self):
            self.parcouru = 0

        def step(self):
            self.robot.vg = 10
            self.robot.vd = 10
            self.parcouru += abs(self.robot.vg*(1./self.FPS))
            if self.stop():
                self.robot.vg=0
                self.robot.vd=0
                return

        def stop(self):
            return self.parcouru>self.distance

  
    class Tourner:
        def __init__(self, angle, robot, FPS = 100):
                self.robot.x = robot.x
                self.robot.y = robot.y
                self.angle = angle
                self.FPS=FPS
            
        

    class TracerCarre:
        def __init__(self, robot, distance, FPS = 100):
            self.robot = robot
            self.distance = distance
            self.FPS=FPS

        def start(self):
            self.parcouru = 0
            
        def step(self):
            if self.stop(): return
            Controleur.AvancerToutDroit.step()
            Controleur.Tourner.step()
            
