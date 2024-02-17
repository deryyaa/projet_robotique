import time

class AvancerToutDroit:
    def __init__(self, robot):
        self.robot = robot

    def avancer_tout_droit(self, distance):
        self.robot.move(10)

class TracerCarre:
    def __init__(self, robot, avancer_tout_droit):
        self.robot = robot
        self.avancer_tout_droit = avancer_tout_droit

    def tracer_carre(self, angle):
        for _ in range(4):
            self.avancer_tout_droit.avancer_tout_droit(angle)
            self.robot.move(90)