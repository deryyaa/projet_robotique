import time
class Controleur:
    class AvancerToutDroit:
        def __init__(self, robot):
            self.robot = robot

        def avancer_tout_droit(self, distance):
            self.robot.vg = 10
            self.robot.vd = 10
            distance_parcouru = 0
            while distance_parcouru<distance :
                self.robot.move(0.1)
                distance_parcouru+=self.robot.vg*0.1 #fps

    class TracerCarre:
        def __init__(self, robot):
            self.robot = robot

        def tracer_carre(self, distance):

            for _ in range(4):
                Controleur.AvancerToutDroit.avancer_tout_droit(distance)
                self.robot.vg = 10
                self.robot.vd =-10