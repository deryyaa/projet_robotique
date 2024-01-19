class Robot:
    def __init__(self,x,y,vitesse=0): #Constructeur
        self.vitesse=vitesse
        self.x=x
        self.y=y
        pass
    pass

    def avancer(self,x1,y1):
        """fonction qui fais avancer le robot"""
        self.x+=x1
        self.y+=y1


#TEST
robot1 = Robot(5,5,5)
robot2 = Robot(5,5)
print(robot1.x,robot1.y)
robot1.avancer(1,1)
print(robot1.x,robot1.y)
print(robot2.vitesse)