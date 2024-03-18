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
        AvancerToutDroit(50,self.robot,self.monde).start()
        robot_x1=self.robot.x
        self.assertEqual(robot_x0,robot_x0+50)

    def test_avancer_tout_droit(self):
        robot_x0=self.robot.dir
        Tourner(50,self.robot,self.monde).start()
        robot_x1=self.robot.dir
        self.assertEqual(robot_x0,robot_x1)

    def test_detecter_collision(self):
        self.assertTrue(self.monde.detecter_collision(15,15))

    def test_pas_de_collision(self):
        self.assertFalse(self.monde.detecter_collision(7,4))
        self.assertFalse(self.monde.detecter_collision(7,4))


    
if __name__ =='__main__':
    unittest.main()
