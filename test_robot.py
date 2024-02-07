import unittest
import math
from futurama.dexter.robot import Robot
from futurama.univers.monde import Monde

#python3 -m unittest test_robot.py -v

#EXEMPLE:
#Pour tout tester :
#python -m unittest discover test -v
#Pour tester un fichier :
#python -m unittest test.test_geo2d -v
#Pour tester une classe de test :
#python -m unittest test.test_geo2d.TestVec2D -v

class Test_Robot(unittest.TestCase):
    def setUp(self):
        self.new_robot=Robot(1,2,3,4,5,6)
        self.new_monde=Monde(20,20)

    def test_avancer(self):
        self.new_robot.avancer()
        self.assertEqual(self.new_robot.vd,5)
        self.assertEqual(self.new_robot.vg,5)
        
    def test_tourner_droite(self):
        self.new_robot.tourner_droite()
        self.assertEqual(self.new_robot.vd,-5)
        self.assertEqual(self.new_robot.vg,5)

    def test_tourner_gauche(self):
        self.new_robot.tourner_gauche()
        self.assertEqual(self.new_robot.vd,5)
        self.assertEqual(self.new_robot.vg,-5)
 
   
if __name__ =='__main__':
    unittest.main()