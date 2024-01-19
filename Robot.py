class Robot:
    def __init__(self,x,y,vitesse=0): # Constructeur
        self.vitesse=vitesse
        self.x=x
        self.y=y
        pass
    pass

    def avancer(self,x1,y1):
        """fonction qui fait avancer le robot"""
        self.x+=x1
        self.y+=y1


# TEST
# creation des robots
robot1 = Robot(5, 5)
robot2 = Robot(5, 5)

# affichage des positions initiales
print("robot 1 :", robot1.x, robot1.y)
print("robot 2 :", robot2.x, robot2.y)

# on fait avancer le premier robot
robot1.avancer(1, 1)

print("apres deplacement")
print("robot 1 :", robot1.x, robot1.y)
print("robot 2 :", robot2.x, robot2.y)

# affichage de la vitesse du deuxieme robot
print("vitesse robot 2 :", robot2.vitesse)