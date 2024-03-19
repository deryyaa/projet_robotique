import unittest
from src.univers.robot import Robot
from src.univers.monde import Monde
from src.controleur.strategie import *

#python3 -m unittest test/test_controleur.py -v

class Test_Strategie(unittest.TestCase):

    def setUp(self):
        self.monde=Monde(20,20)
        self.robot=Robot(10,10,4,4,5,6)

    def test_avancer_tout_droit(self):
        robot_x0=self.robot.x
        print(robot_x0)
        AvancerToutDroit(50,self.robot,self.monde).step()
        robot_x1=self.robot.x
        print(robot_x1)
        self.assertEqual(robot_x1,robot_x0+50)
        self.assertEqual(robot_x0,robot_x1-50)


if __name__ =='__main__':
    unittest.main()
