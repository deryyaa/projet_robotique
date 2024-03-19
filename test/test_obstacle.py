import unittest
from src.univers.obstacle import Obstacle

class TestObstacle(unittest.TestCase):
    def setUp(self):
        self.obst = Obstacle(15, 15, 1, 1)
    
    def test_getPosition(self):
        """teste si la fonction getPosition de Obstacle"""
        self.assertEqual(self.obst.getPosition(), (15, 15))
    
    def test_getRect(self):
        """teste si la fonction getPosition de Obstacle"""
        self.assertEqual(self.obst.getRect(), [[14.5, 14.5], [15.5, 14.5], [15.5, 15.5], [14.5, 15.5]])

if __name__ == '__main__':
    unittest.main()
    