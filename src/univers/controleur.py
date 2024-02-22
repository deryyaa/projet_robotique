import time
class Controleur:
    class AvancerToutDroit:
        def __init__(self, robot, FPS = 100):
            self.robot = robot
            self.FPS = FPS

        def avancer_tout_droit(self, distance):
            self.robot.vg = 10
            self.robot.vd = 10
            distance_parcouru = 0
            while distance_parcouru<distance :
                if (self.robot.capteur_distance()<1):
                    self.robot.move(1./self.FPS)
                    distance_parcouru+=self.robot.vg*(1./self.FPS)

    class Tourner:
        def __init__(self, robot):
            self.robot = robot

        def tourner(self, degre):
            self.robot.vg = 10
            self.robot.vd = -10
            distance_parcouru = 0
            while distance_parcouru<degre :
                if (self.robot.capteur_distance()<1):
                    self.robot.move(1./self.FPS)
                    distance_parcouru+=self.robot.vg*(1./self.FPS)

        
    class TracerCarre:
        def __init__(self, robot):
            self.robot = robot

        def tracer_carre(self, distance):

            for _ in range(4):
                Controleur.AvancerToutDroit.avancer_tout_droit(distance)
                Controleur.Tourner.tourner()

    