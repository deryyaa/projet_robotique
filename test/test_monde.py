import unittest
import math
from src.univers.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle

#python3 -m unittest test/test_monde.py -v

class Test_Monde(unittest.TestCase):
    def setUp(self):
        self.monde=Monde(20,20)
        self.robot=Robot(10,10,4,4,5,6)
        self.monde.creation_obstacle(15,15,1,1)
        print(self.monde.obstacles)

    def test_detecter_collision(self):
        self.assertTrue(self.monde.detecter_collision(15,15))

    def test_pas_de_collision(self):
        self.assertFalse(self.monde.detecter_collision(7,4))
        self.assertFalse(self.monde.detecter_collision(7,4))
         

if __name__ =='__main__':
    unittest.main()