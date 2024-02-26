import time
class Controleur:
    class AvancerToutDroit:
        def __init__(self, robot, distance, FPS = 100):
            self.robot = robot
            self.distance = distance
            self.FPS = FPS

        def start(self):
            self.parcouru = 0

        def stop(self):
            return self.parcouru>self.distance
        
        def step(self):
            self.robot.vg = 10
            self.robot.vd = 10
            self.parcouru += self.robot.vg*(1./self.FPS)
            if self.stop(): return
            self.robot.move(1./self.FPS)


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
        def __init__(self, robot):
            self.robot = robot

        def start(self):
            
            Controleur.AvancerToutDroit.avancer_tout_droit(dist=10)
            
