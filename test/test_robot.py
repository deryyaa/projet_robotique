import unittest
import math
from src.univers.robot import Robot
from src.univers.monde import Monde

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
        self.new_robot=Robot(1,2,3,4,5,6)
        self.new_monde=Monde(20,20)

   
if __name__ =='__main__':
    unittest.main()




