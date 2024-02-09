import unittest
import math
from futurama.dexter.robot import Robot
from futurama.univers.monde import Monde
from futurama.univers.obstacle import Obstacle

#python3 -m unittest test_monde.py -v

class Test_Monde(unittest.TestCase):
    def setUp(self):
        self.monde=Monde(20,20)
        self.robot=Robot(10,10,4,4,5,6)
        self.obstacle=Obstacle(15,15,1,1)

    def test_peut_avancer(self):
        self.assertTrue(self.monde.peut_avancer(1,1,self.robot))
        self.robot.avancer_(8,self.monde)
        print(self.robot.x,self.robot.y, self.monde.peut_avancer(1,1,self.robot))
        self.assertFalse(self.monde.peut_avancer(1,1,self.robot))






if __name__ =='__main__':
    unittest.main()