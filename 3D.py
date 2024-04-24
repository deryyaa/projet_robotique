import tkinter as tk
import math

# Fonction pour effectuer une projection en perspective
def project(point):
    x, y, z = point
    distance = 400  # Distance entre le plan de projection et l'origine
    scale = distance / (distance + z)
    return (200 + scale * x, 200 - scale * y)

# Fonction pour dessiner un cube en 3D rempli
def draw_filled_cube(canvas):
    # Coordonnées des sommets du cube
    vertices = [
        (-50, -50, -50),
        (50, -50, -50),
        (50, 50, -50),
        (-50, 50, -50),
        (-50, -50, 50),
        (50, -50, 50),
        (50, 50, 50),
        (-50, 50, 50)
    ]
    # Faces du cube
    faces = [
        (0, 1, 2, 3),  # Face avant
        (4, 5, 6, 7),  # Face arrière
        (0, 1, 5, 4),  # Côté gauche
        (2, 3, 7, 6),  # Côté droit
        (0, 3, 7, 4),  # Haut
        (1, 2, 6, 5)   # Bas
    ]
    # Dessiner les faces du cube
    for face in faces:
        points = [project(vertices[vertex]) for vertex in face]
        canvas.create_polygon(points, fill="gray", outline="black")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Cube 3D rempli")

# Création du canevas pour dessiner le cube
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Dessiner le cube rempli
draw_filled_cube(canvas)

# Lancer la boucle principale
root.mainloop()
