import unittest
import math
from src.univers.robot import Robot
from src.univers.monde import collision_rect, Monde
from src.univers.obstacle import Obstacle

#python3 -m unittest test/test_monde.py -v

class Test_Monde(unittest.TestCase):
    def setUp(self):
        self.robot=Robot(10,10,4,4,5,6)
        self.monde=Monde(20,20,self.robot)
        self.monde.creation_obstacle(15,15,1,1)
        print(self.monde.obstacles)


    def test_collision_rect(self):
        rectangle_obstacle = [(10, 20), (30, 40), (30, 40),(30,40)]  
        rectangle_robot = [(10, 20), (30, 40), (30, 40),(30,40)]  
        self.assertTrue(collision_rect(rectangle_obstacle,rectangle_robot))

    def test_creation_obstacle(self):
        x, y, largeur, longueur = 10, 20, 5, 3
        self.monde.creation_obstacle(x, y, largeur, longueur)
        self.assertEqual(len(self.monde.obstacles), 2, "L'obstacle n'a pas été ajouté à la liste")

        # Vérifie si les attributs de l'obstacle sont corrects
        obstacle_ajoute = self.monde.obstacles[1]
        self.assertEqual(obstacle_ajoute.x, x, "Coordonnée x incorrecte")
        self.assertEqual(obstacle_ajoute.y, y, "Coordonnée y incorrecte")
        self.assertEqual(obstacle_ajoute.longueur, longueur, "Longueur incorrecte")
        self.assertEqual(obstacle_ajoute.largeur, largeur, "Largeur incorrecte")
    
    def test_detecter_collision(self):
        self.assertFalse(self.monde.detecter_collision(5, 5))
    
    def test_place_obstacle(self):
        self.assertTrue(self.monde.detecter_collision(380, 200))  # Vérifiez l'obstacle à (380, 200)
        self.assertTrue(self.monde.detecter_collision(250, 1))    # Vérifiez le mur du bas
        self.assertTrue(self.monde.detecter_collision(1, 250))    # Vérifiez le mur de gauche
        self.assertTrue(self.monde.detecter_collision(250, 499))  # Vérifiez le mur du haut
        self.assertTrue(self.monde.detecter_collision(500, 250))  # Vérifiez le mur de droite
        
    def test_creation_monde(self):
        self.assertEqual(self.monde.ligne, 20)
        self.assertEqual(self.monde.colonne, 20)
        self.assertEqual(self.monde.robot, self.robot)

if __name__ =='__main__':
    unittest.main()