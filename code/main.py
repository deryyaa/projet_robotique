from Robot import Robot
from Monde import Monde
robot1 = Robot(5,5,1,1,1,180)
monde = Monde(10,20)
monde.setRobot(robot1)


monde.affiche()
print(robot1.x,robot1.y)
robot1.avance(monde)
monde.affiche()
print(robot1.x,robot1.y)