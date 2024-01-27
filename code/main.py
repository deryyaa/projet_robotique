from Robot import Robot
from Monde import Monde
from random import randint
from time import sleep

robot1 = Robot(5, 5, 1, 1, 1, 180)
monde = Monde(10, 20)
monde.setRobot(robot1)

for _ in range(100):
    direction = randint(0, 3)  # 0: Avancer, 1: Reculer, 2: Tourner à gauche, 3: Tourner à droite

    if direction == 0:
        robot1.avancer(1, monde)
    elif direction == 1:
        robot1.reculer(1, monde)
    elif direction == 2:
        robot1.tourner_gauche(10)
    else:
        robot1.tourner_droite(10)

    # Affichage des coordonnées avec deux chiffres après la virgule
    #print("x : {:.2f}, y : {:.2f}".format(robot1.x, robot1.y))
    monde.affiche()

    # Temps de repos de 1 seconde entre chaque itération
    sleep(0.2)
