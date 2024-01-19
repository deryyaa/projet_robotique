class Robot:
    def __init__(self,x,y,vitesse=0): #Constructeur
        self.vitesse=vitesse
        self.x=x
        self.y=y
        pass
    pass
    


#TEST
robot1 = Robot(5,5,5)
robot2 = Robot(5,5)

print(robot1.vitesse)
print(robot2.vitesse)