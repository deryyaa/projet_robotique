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
                return 0

        def stop(self):
            return self.parcouru>self.distance

    class Tourner:
        def __init__(self, robot, distance, FPS = 100):
            self.robot = robot
            self.distance = distance
            self.FPS=FPS

        def start(self):
            self.parcouru = 0

        def step(self):
            self.robot.vg = 10
            self.robot.vd = -10
            self.parcouru += self.robot.vg*(1./self.FPS)
            if self.stop(): return
            self.robot.move(1./self.FPS)
            
            #if (self.robot.capteur_distance()<1):
      
        def stop(self):
            return self.parcouru>self.distance

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
            
