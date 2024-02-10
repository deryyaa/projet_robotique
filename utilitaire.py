def collision_rect(r1,r2): #prend en parametre une liste de tuple des 2 coordonnées de mon rectangle (obstacle et robot)
    """renvoie True quand les 2 rectangle r1,r2 se superpose"""
    # Déballage des tuples pour obtenir les coordonnées et dimensions des rectangles
    x1,y1,w1,h1 = r1[0][0], r1[0][1], r1[1][0] - r1[0][0], r1[1][1] - r1[0][1]
    x2,y2,w2,h2= r2[0][0], r2[0][1], r2[1][0] - r2[0][0], r2[1][1] - r2[0][1]
    # Vérification de la superposition des rectangles
    # La superposition est vérifiée en négatif, donc si l'une des conditions est vraie, la superposition n'a pas lieu.

    return [True,False][x1 >= x2 + w2 or x1 + w1 <= x2 or y1 >= y2 + h2 or y1 + h1 <= y2]


def distance_points(p1, p2):
        """Calcule la distance euclidienne entre deux points"""
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

