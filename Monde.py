class Monde:
    def __init__(self,ligne,colonne):
        """ constructeur """
        self.ligne=ligne
        self.colonne=colonne

    def affiche(self):
        """fonction qui permet d'afficher le monde dans le terminale"""
        a="+"+"-"*self.colonne+"+"+"\n"
        for i in range(self.ligne):
            a+="|"
            for j in range(self.colonne):
                a+=" "
            a+="|\n"

        a+="+"+"-"*self.colonne+"+"+"\n"
        print(a)



m1 = Monde(9,45)
m1.affiche() 