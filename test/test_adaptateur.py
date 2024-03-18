import unittest
import math
from src.univers.robot import Robot
from src.univers.monde import collision_rect, Monde
from src.univers.obstacle import Obstacle
from src.univers.adaptateur import Robot2I013Adaptateur

class Test_Robot2I013Adaptateur(unittest.TestCase):
    def setUp(self):
        # Créez un robot fictif (vous devrez adapter cela à votre implémentation)
        self.robot=Robot(10,10,4,4,5,6)   # Remplacez par le nom de votre classe Robot
        self.adaptateur = Robot2I013Adaptateur(self.robot)

    def test_move(self):
        # Testez le déplacement du robot
        dt = 0.1  # Exemple de pas de temps
        self.adaptateur.setVitesse(10, 10)  # Définissez une vitesse arbitraire
        self.adaptateur.move(dt)
        # Vérifiez si les coordonnées ont changé (vous devrez adapter cela)
        #self.assertNotEqual(self.adaptateur.getPosition(), (0, 0))
        print(self.adaptateur.x,self.adaptateur.x)

    

if __name__ == "__main__":
    unittest.main()