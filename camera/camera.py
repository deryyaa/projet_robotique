import cv2
import numpy as np

# Chemin du fichier avec double antislashs
image_path = 'C:\\Users\\nutella\\Documents\\LICENCE 2\\S2\\PROJET DE DEV\\projet_robotique\\camera\\pattern.jpg'

# Lire l'image
img = cv2.imread(image_path, 1)
img = cv2.resize(img,(500,500))
img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

# Vérifier si l'image a été chargée correctement
if img is None:
    print(f"Erreur: Impossible de charger l'image à partir de {image_path}")
else:
    # Afficher l'image
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Réprésentation image en pixel
print(img)
#print(img.shape)

# Initialiser la capture vidéo (0 pour la caméra par défaut)
cap = cv2.VideoCapture(0)

while True:
    # Lire une frame de la capture vidéo
    ret, frame = cap.read()
    if not ret:
        print("Erreur: Impossible de lire une frame de la caméra")
        break

   
    # Redimensionner la frame à la moitié de sa taille
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    print("valeurs des pixels de l'image:")
    print(smaller_frame)

    # Afficher l'image résultante
    cv2.imshow('camera_frame', smaller_frame)

    # Parcourir chaque pixel de l'image
    for row in smaller_frame:
        for pixel in row:
            # Vérifier si le pixel est bleu
            if pixel[0] > 100 and pixel[1] < 100 and pixel[2] < 100:
                print("Bleu détecté")
                
    # Attendre une touche pendant 1 milliseconde
    if cv2.waitKey(1) == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()