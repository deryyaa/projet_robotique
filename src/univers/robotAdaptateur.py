from robot import Robot

class RobotAdaptateur(Robot):
    def __init__(self, x, y, longueur, largeur, vitesse_max, dir=0):
        Robot.__init__(self, x, y, longueur, largeur, vitesse_max,dir)
    

    def setVitesseRoue(self,vrg,vrd):
        Robot.vg=vrg
        Robot.vd=vrd
    
