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
        self.obstacle = Obstacle(380,200,50,50)

    def test_getposition(self):
        pos = (self.new_robot.x, self.new_robot.y)
        self.assertEqual(self.new_robot.getPosition(), pos)
    
    def test_getRect(self):
        corps = [[self.new_robot.x-self.new_robot.longueur/2 ,self.new_robot.y-self.new_robot.largeur/2], [self.new_robot.x+self.new_robot.longueur/2 ,self.new_robot.y-self.new_robot.largeur/2], [self.new_robot.x+self.new_robot.longueur/2 ,self.new_robot.y+self.new_robot.largeur/2], [ self.new_robot.x-self.new_robot.longueur/2 ,self.new_robot.y+self.new_robot.largeur/2]]
        self.assertEqual(self.new_robot.getRect(),corps)

    def test_setvitesse(self):
        vitesse = self.new_robot.setVitesse(10,10)
        self.assertEqual( (10,10), (self.new_robot.vd, self.new_robot.vg))

    def test_capteur_distance(self):
        self.assertEqual(self.new_robot.capteur_distance(self.new_monde),51)

    def test_move_getdistance(self):
        self.assertEqual(self.new_robot.distanceParcouru,self.new_robot.getDistanceParcouru())
        self.new_robot.setVitesse(10,10)
        self.new_robot.move(10)
        self.assertEqual(self.new_robot.distanceParcouru,self.new_robot.getDistanceParcouru())

if __name__ =='__main__':
    unittest.main()




