from Robot import Robot
from Monde import Monde

# TEST CLASSE ROBOT
print("test robot")
# creation des robots
robot1 = Robot(0, 0) # creation d'un robot en point x, y
robot2 = Robot(0, 0)
monde = Monde(10,20) # creation d'un monde x*y

# affichage des positions initiales
print("robot 1 :", robot1.x, robot1.y)
print("robot 2 :", robot2.x, robot2.y)

# on fait avancer le premier robot
robot1.avancer(monde, 1, 1)

# affichage de la vitesse du deuxieme robot
print("vitesse robot 2 :", robot2.vitesse)

#TEST CLASSE MONDE
"""
monde.setRobot(robot2)
monde.affiche() # affiche le monde
robot2.avancer(monde,5,5) # fait avancer le robot
monde.setRobot(robot2) # ajoute le robot au monde
monde.affiche() """

# AUTRE TEST

print("\n")
print("test monde") 

monde.setRobot(robot2)

while True:
    resultat = robot2.avancer(monde, 1.5, 2)
    if resultat == "mur":
        print("Le robot a rencontré un mur !")
        break
    else :
        monde.affiche()

print("\napres deplacement")
print("robot 1 :", robot1.x, robot1.y)
print("robot 2 :", robot2.x, robot2.y)