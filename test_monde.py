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
        # Vérifie si le robot peut avancer sans dépasser les limites du monde
        self.assertTrue(self.monde.peut_avancer(1, 1, self.robot))
        self.assertFalse(self.monde.peut_avancer(20, 20, self.robot))
        self.assertFalse(self.monde.peut_avancer(-10, -10, self.robot))

    
    def test_detecter_collision(self):
        monde=Monde(20,20)
        obstacle1= Obstacle(10,17,5,5)
        obstacle2= Obstacle(15,17,5,5)
        robot=Robot(12,19,2,2,20)
        monde.setObstacle(obstacle1)
        monde.setObstacle(obstacle2)
        self.assertTrue(monde.detecter_collision(robot))

    def test_pas_de_collision(self):
        monde= Monde(20,20)
        robot= Robot(12,19,2,2,20)
        self.assertFalse(monde.detecter_collision(robot))

        obstacle3 = Obstacle(18,30,4,4)
        obstacle4 = Obstacle(20,28,3,3)
        monde.setObstacle(obstacle3)
        monde.setObstacle(obstacle4)
        self.assertFalse(monde.detecter_collision(robot))
         

if __name__ =='__main__':
    unittest.main()