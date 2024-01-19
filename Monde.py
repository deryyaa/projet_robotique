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