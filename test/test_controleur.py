import unittest
from src.dexter.robot import Robot
from src.univers.monde import Monde
from controleur import Controleur

#python3 -m unittest test/test_controleur.py -v

class Test_Monde(unittest.TestCase):
    def setUp(self):
        self.monde=Monde(20,20)
        self.robot=Robot(10,10,4,4,5,6)
        self.monde.setRobot(self.robot)
        controleur = Controleur(self.robot)

    def test_avancer(self):
        self.controleur.avancer(distance=50)
        self.assertEqual(self.robot.x,50)
        self.assertEqual(self.robot.y,50)

    def test_augmenter_vitesse_gauche(self):
        self.controleur.augmenter_vitesse_gauche(n=5)
        self.assertEqual(self.robot.augmenter_vg,5)


    def test_deplacer(self):
        self.controleur.deplacer(distance=20, temps=5)
        self.assertEqual()


if __name__ =='__main__':
    unittest.main()
