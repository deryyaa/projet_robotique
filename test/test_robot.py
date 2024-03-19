import unittest
import math
from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle

#python3 -m unittest test/test_robot.py -v

#EXEMPLE:
#Pour tout tester :
#python -m unittest discover test -v
#Pour tester un fichier :
#python -m unittest test.test_geo2d -v
#Pour tester une classe de test :
#python -m unittest test.test_geo2d.TestVec2D -v

class Test_Robot(unittest.TestCase):

    def setUp(self):
        self.new_robot= Robot.creation_robot()
        self.new_monde=Monde(500,500,self.new_robot)
        self.obstacle = self.new_monde.creation_obstacle(380,200,50,50)

    def test(self):
        """ test unitaire de getposition(), move(), getDistanceParcouru(), getRect(), setVitesse() """
        print("position initiale: ", self.new_robot.getPosition())
        print("position du corps du robot:", self.new_robot.getRect())
        
        self.new_robot.move(1)
        
        print("position apres le mouvement:", self.new_robot.getPosition()," distance parcouru: ",self.new_robot.getDistanceParcouru())
        print("position du corps du robot:", self.new_robot.getRect())

    def test_setvitesse(self):
        print("test_setvitesse")
        print("vitesse initiale:", self.new_robot.vd, self.new_robot.vg)
        self.new_robot.setVitesse(10,10)
        print("vitesse apres setvitesse:", self.new_robot.vd, self.new_robot.vg)
    
    def test_capteur_distance(self):
        print("test_capteur_distance")
        self.new_robot.capteur_distance(self.new_monde)

if __name__ =='__main__':
    unittest.main()




