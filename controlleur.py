class Controleur:
    def __init__(self, vitesse, direction):
        """Initialise le contrôleur avec une vitesse et une direction"""
        self.vitesse = vitesse
        self.direction = direction

    def set_vitesse(self, vitesse):
        """Definit la vitesse du contrôleur"""
        self.vitesse = vitesse

    def set_direction(self, direction):
        """Definit la direction du contrôleur"""
        self.direction = direction