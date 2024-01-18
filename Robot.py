class Robot:
    def __init__(self, vitesse=0): #Constructeur
        self.vitesse=vitesse
        pass
    pass

#TEST
robot1 = Robot(15)
robot2 = Robot()

print(robot1.vitesse)
print(robot2.vitesse)