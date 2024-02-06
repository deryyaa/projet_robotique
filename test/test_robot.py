import unittest
import math
from ..projet.robot.robot import Robot
from ..projet.univers.monde import Monde
#python3 -m unittest test/test_robot.py -v
class Test_Robot(unittest.TestCase):
    def setUp(self):
        self.new_robot=Robot(1,2,3,4,5,6)
        self.new_monde=Monde(20,20)

    def test_avancer(self):
        x=self.new_robot.x
        y=self.new_robot.y
        self.new_robot.avancer(10,self.new_monde)
        new_x=self.new_robot.x
        new_y=self.new_robot.y
        self.assertEqual(new_x-x,10 * math.cos(math.radians(self.new_robot.dir)))
        self.assertEqual(new_y-y,10 * math.cos(math.radians(self.new_robot.dir)))


    def test_tourner_droite(self):
        dir=self.new_robot.dir
        self.new_robot.tourner_droite(13)
        new_dir=self.new_robot.dir
        self.assertEqual(new_dir,dir-13%360)

    def test_tourner_gauche(self):
        dir=self.new_robot.dir
        self.new_robot.tourner_droite(13)
        new_dir=self.new_robot.dir
        self.assertEqual(new_dir,dir+13%360)
 
   
if __name__ =='__main__':
    unittest.main()