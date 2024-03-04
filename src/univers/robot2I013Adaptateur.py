from robot2I013 import Robot2IN013

class Robot2I013Adaptateur(Robot2IN013):
    def __init__(self,nb_img=10,fps=25,resolution=None,servoPort = "SERVO1",motionPort="AD1"):
        Robot2IN013.__init__(self,nb_img,fps,resolution,servoPort,motionPort)