from .robotReel import Robot2IN013
import math

class Robot2I013Adaptateur():
    def __init__(self,robot,x,y):
        self.robot=robot
        self.x=x
        self.y=y
        self.vg=1
        self.vd=1
        self.dir=0
        self.distanceParcouru=0
        
    def move(self,dt):
        x=self.x
        y=self.y
        self.x += ((self.vg*dt+self.vd*dt)/2.0) * math.cos(self.dir)
        self.y += ((self.vg*dt+self.vd*dt)/2.0) * math.sin(self.dir)
        if(self.vg!=self.vd):
            if(abs(self.vg)>abs(self.vd)):
                self.dir-=self.vg*dt/(-self.d*self.vg*dt/(self.vd*dt-self.vg*dt))
            else:
                self.dir+=self.vd*dt/(-self.d*self.vd*dt/(self.vg*dt-self.vd*dt))
        self.distanceParcouru+=math.sqrt((self.x-x)**2+(self.y-y)**2)

        
    def setVitesse(self, vg,vd):
        self.vg=vg
        self.robot.set_motor_dps(self.robot.MOTOR_LETF,vg)
        self.vd=vd
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,vd)

    def getPosition(self):
        return (self.x,self.y)
    
    def getDistanceParcouru(self):
        return self.distanceParcouru

    def capteur_distance(self,monde):
        return self.robot.get_distance()