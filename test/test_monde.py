import unittest
import math
from src.dexter.robot import Robot
from src.univers.monde import Monde
from src.univers.obstacle import Obstacle

#python3 -m unittest test/test_monde.py -v

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
        obstacle1= Obstacle(2,1,4,2)
        obstacle2= Obstacle(6,3,3,2)
        self.monde.setObstacle(obstacle1)
        self.monde.setObstacle(obstacle2)
        self.assertTrue(self.monde.detecter_collision(3,2))

    def test_pas_de_collision(self):
        self.assertFalse(self.monde.detecter_collision(7,4))
        obstacle3= Obstacle(2,1,4,2)
        obstacle4= Obstacle(6,3,3,2)
        self.monde.setObstacle(obstacle3)
        self.monde.setObstacle(obstacle4)
        self.assertFalse(self.monde.detecter_collision(7,4))
         

if __name__ =='__main__':
    unittest.main()