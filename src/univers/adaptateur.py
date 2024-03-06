from robot2I013 import Robot2IN013

class Robot2I013Adaptateur():
    def __init__(robot):
        self.robot=robot

    
    def setVitesse(self, vg,vd):
        self.robot.set_motor_dps(self.robot.MOTOR_LETF,vg)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vd)

    def getPosition():
        return self.robot.get_motor_position()