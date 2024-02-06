from ..projet.robot.robot import Robot
from ..projet.univers.monde import Monde
from ..projet.univers.obstacle import Obstacle
from random import randint
from time import sleep

# Création du monde
monde = Monde(10, 20)

# Création des obstacles
obstacle1 = Obstacle(2, 2, 1, 1)
obstacle2 = Obstacle(8, 18, 1, 1)
monde.setObstacle(obstacle1) # Ajout d'obstacles au monde
monde.setObstacle(obstacle2)
for i in range(5):
    monde.setObstacle(Obstacle(2+i+1, 2, 1, 1)) #creation de plusieurs obstacle pour crée une colision
robot1 = Robot(5, 5, 1, 1, 1, 180)
monde.setRobot(robot1)

for _ in range(100):
    direction = randint(0, 3)  # 0: Avancer, 1: Reculer, 2: Tourner à gauche, 3: Tourner à droite

    if direction == 0 and not (robot1.x + 1 == obstacle1.x and robot1.y == obstacle1.y):  # Vérifie si le prochain mouvement ne heurte pas l'obstacle
        #robot1.avancer(1, monde)
        monde.avancer_robot(1,robot1)
    elif direction == 1 and not (robot1.x - 1 == obstacle1.x and robot1.y == obstacle1.y):
        monde.avancer_robot(-1,robot1)
    elif direction == 2:
        robot1.tourner_gauche(10)
    elif direction == 3:
        robot1.tourner_droite(10)

    monde.affiche()

    # Temps de repos de 0.1 seconde entre chaque itération
    sleep(0.1)

# Affichage des coordonnées avec deux chiffres après la virgule
print("x : {:.2f}, y : {:.2f}".format(robot1.x, robot1.y))
