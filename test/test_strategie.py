import unittest
from src.univers.robot import Robot
from src.univers.monde import Monde
from src.controleur.strategie import *

#python3 -m unittest test/test_strategie.py -v

class Test_Strategie(unittest.TestCase):

    def setUp(self):
        self.monde=Monde(20,20)
        self.robot=Robot(10,10,4,4,5,6)
        self.strategie=AvancerToutDroit(50,self.robot,self.monde)

    def test_avancer_tout_droit(self):
        self.strategie.start()
        while not self.strategie.stop():
            self.strategie.step()
            self.assertNotEqual(self.strategie.distance, 0)
        self.assertEqual(self.strategie.distance, 0)


if __name__ =='__main__':
    unittest.main()
