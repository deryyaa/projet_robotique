from Robot import Robot
class Monde:
    def __init__(self,ligne,colonne):
        """ constructeur """
        self.ligne=ligne # initialisation des coordonnes
        self.colonne=colonne
        self.robot=None

    def affiche(self):
        """fonction qui permet d'afficher le monde dans le terminale"""
        a="+"+"-"*self.colonne+"+"+"\n"
        for i in range(self.ligne):
            a+="|"
            for j in range(self.colonne):
                if self.robot!=None and self.robot.x==i and self.robot.y==j:
                    a+="X"
                else:
                    a+=" "
            a+="|\n"

        a+="+"+"-"*self.colonne+"+"+"\n"
        print(a) 

    def setRobot(self, robot):
        self.robot=robot # initialisation du robot

#TEST

robot= Robot(1,20) # creation d'un robot en point x, y
m1 = Monde(9,45) # creation d'un monde x*y
m1.setRobot(robot)
m1.affiche() # affiche le monde
robot.avancer(5,5) # fait avancer le robot
m1.setRobot(robot)
m1.affiche()

# AUTRE TEST 
# manque la condition pour ne pas depasser le mur à avancer (rash)
robot= Robot(0,0)
m1 = Monde(9,45)
m1.setRobot(robot)
m1.affiche()
for i in range (20):
    robot.avancer(1,1)
    m1.affiche()