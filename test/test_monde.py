import unittest
import math
from ..robot.robot import Robot
from ..univers.monde import Monde
from ..univers.obstacle import Obstacle

class Test_Monde(unittest.TestCase):
    def setUp(self):
        self.new_monde=Monde(20,20)
        self.new_robot=Robot(10,10,3,4,5,6)
        self.obstacle=Obstacle(15,15,1,1)

    def test_peut_avancer(self):
        self.assertTrue(self.new_monde.peut_avancer(1,1,self.new_robot)) 
        self.new_robot.avancer(10,self.new_monde)
        self.assertFalse(self.new_monde.peut_avancer(1,1,self.new_robot))

    def test_avancer_robot(self):
        self.new_robot.avancer(-10,self.new_monde)
        self.new_monde.avancer_robot(5,self.new_robot)
        x=self.new_robot.x
        y=self.new_robot.y
        self.assertEqual(x,self.obstacle.x-1)
        self.assertEqual(y,self.obstacle.y-1)
if __name__ =='__main__':
    unittest.main()