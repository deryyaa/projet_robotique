import unittest
import math
from src.univers.robot import Robot
from src.univers.monde import collision_rect, Monde
from src.univers.obstacle import Obstacle

#python3 -m unittest test/test_monde.py -v

class Test_Monde(unittest.TestCase):
    def setUp(self):
        self.monde=Monde(20,20)
        self.robot=Robot(10,10,4,4,5,6)
        self.monde.creation_obstacle(15,15,1,1)
        print(self.monde.obstacles)


    def test_collision_rect(self):
        rectangle_obstacle = [(10, 20), (30, 40), (30, 40),(30,40)]  
        rectangle_robot = [(10, 20), (30, 40), (30, 40),(30,40)]  
        self.assertTrue(collision_rect(rectangle_obstacle,rectangle_robot))
        

if __name__ =='__main__':
    unittest.main()