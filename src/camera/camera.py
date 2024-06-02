import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import math
import imageio
import sys

def resize_img(img):
    """
    Redimensionne l'image à une taille de 200x200 pixels.

    Arguments:
    img : le chemin de l'image à lire et redimensionner

    Retourne:
    L'image redimensionnée ou None si l'image n'a pas pu être lue.
    """
    img = cv.imread(img, 1) 
    if img is None:
        print("Erreur: Impossible de lire l'image. Vérifiez le chemin du fichier.") 
        return None
    else:
        return cv.resize(img, (200, 200))  

def segmenter_couleur(hsv, lower, upper):
    """
    Segmente une couleur spécifique dans une image HSV et calcule le barycentre de la région segmentée.

    Arguments:
    hsv : l'image HSV
    lower : les limites inférieures de la couleur à segmenter
    upper : les limites supérieures de la couleur à segmenter

    Retourne:
    L'image segmentée et les coordonnées du barycentre.
    """
    seg = cv.inRange(hsv, lower, upper)  # Segmente la couleur en utilisant les limites fournies
    median_seg = cv.medianBlur(seg, 9)  #Applique un flou médian pour réduire le bruit
    moments = cv.moments(median_seg) 
    if moments['m00'] != 0:
        cX = int(moments['m10'] / moments['m00']) 
        cY = int(moments['m01'] / moments['m00'])  
    else:
        cX, cY = 0, 0 
    return median_seg, (cX, cY)  

def afficher_resultat(image, barycentre, couleur, title):
    """
    Affiche une image segmentée avec le barycentre marqué.

    Arguments:
    image : l'image segmentée
    barycentre : les coordonnées du barycentre
    couleur : la couleur du marqueur de barycentre
    title : le titre de l'image
    """
    plt.figure(figsize=(4, 4))
    plt.imshow(image, cmap='gray') 
    plt.scatter(barycentre[0], barycentre[1], color=couleur, s=50, marker='x')  # Marque le barycentre avec un 'x'
    plt.title(title) 

def verifier_adjacence(barycentre1, barycentre2, seuil):
    """
    Vérifie si deux barycentres sont adjacents en fonction d'un seuil de distance.

    Arguments:
    barycentre1 : les coordonnées du premier barycentre
    barycentre2 : les coordonnées du deuxième barycentre
    seuil : la distance maximale pour considérer que les barycentres sont adjacents

    Retourne:
    True si les barycentres sont adjacents, False sinon.
    """
    distance = math.sqrt((barycentre2[0] - barycentre1[0])**2 + (barycentre2[1] - barycentre1[1])**2)  # Calcule la distance entre les deux barycentres
    return round(distance) < seuil 

def isBalise(image):
    """
    Vérifie si une image contient une balise composée de quatre couleurs (rouge, jaune, vert et bleu).

    Arguments:
    image : le chemin de l'image à vérifier

    Retourne:
    True si la balise est présente, False sinon.
    """
    img = resize_img(image) 
    
    if img is not None:
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # Convertit l'image en espace de couleurs HSV
        
        # Rouge
        lower_red1 = np.array([0, 190, 0], dtype=np.uint8)
        upper_red1 = np.array([15, 255, 255], dtype=np.uint8)
        seg_red1 = cv.inRange(hsv, lower_red1, upper_red1)  # Segmente le rouge dans la première plage de teinte
        lower_red2 = np.array([340/2, 190, 0], dtype=np.uint8)
        upper_red2 = np.array([360/2, 255, 255], dtype=np.uint8)
        seg_red2 = cv.inRange(hsv, lower_red2, upper_red2)  # Segmente le rouge dans la deuxième plage de teinte

        seg_red = cv.bitwise_or(seg_red1, seg_red2)  # Combine les deux segmentations rouges
        median_seg_red = cv.medianBlur(seg_red, 9)  
        moments = cv.moments(median_seg_red)  

        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00']) 
            cY = int(moments['m01'] / moments['m00']) 
        else:
            cX, cY = 0, 0 
        
        centre_rouge = (cX, cY)  

        # Jaune
        lower_yellow = np.array([36/2, 180, 0], dtype=np.uint8)
        upper_yellow = np.array([60/2, 255, 255], dtype=np.uint8)
        seg_yellow, centre_jaune = segmenter_couleur(hsv, lower_yellow, upper_yellow)  # Segmente le jaune et calcule le barycentre
        
        # Vert
        lower_green = np.array([70/2, 0, 0], dtype=np.uint8)
        upper_green = np.array([180/2, 255, 255], dtype=np.uint8)
        seg_green, centre_vert = segmenter_couleur(hsv, lower_green, upper_green)  # Segmente le vert et calcule le barycentre
        
        # Bleu
        lower_blue = np.array([190/2, 190, 0], dtype=np.uint8)
        upper_blue = np.array([255/2, 255, 255], dtype=np.uint8)
        seg_blue, centre_bleu = segmenter_couleur(hsv, lower_blue, upper_blue)  # Segmente le bleu et calcule le barycentre

        # Seuils de distance pour chaque paire de couleurs voisines
        seuil_jaune_vert = 71
        seuil_vert_bleu = 64
        seuil_bleu_rouge = 70
        seuil_rouge_jaune = 64

        # Vérifier l'adjacence entre les barycentres des zones de couleur
        adjacence_jaune_vert = verifier_adjacence(centre_jaune, centre_vert, seuil_jaune_vert)
        adjacence_vert_bleu = verifier_adjacence(centre_vert, centre_bleu, seuil_vert_bleu)
        adjacence_bleu_rouge = verifier_adjacence(centre_bleu, centre_rouge, seuil_bleu_rouge)
        adjacence_rouge_jaune = verifier_adjacence(centre_rouge, centre_jaune, seuil_rouge_jaune)

        # Afficher les résultats
        print("Jaune est à côté de Vert et Rouge :", adjacence_jaune_vert and adjacence_rouge_jaune)
        print("Vert est à côté de Bleu et Jaune :", adjacence_vert_bleu and adjacence_jaune_vert)
        print("Bleu est à côté de Vert et Rouge :", adjacence_bleu_rouge and adjacence_vert_bleu)
        print("Rouge est à côté de Jaune et Bleu :", adjacence_rouge_jaune and adjacence_bleu_rouge)

        # Afficher les images segmentées avec les barycentres
        # afficher_resultat(seg_red, centre_rouge, 'red', "Rouge avec Barycentre")
        # afficher_resultat(seg_yellow, centre_jaune, 'yellow', "Jaune avec Barycentre")
        # afficher_resultat(seg_green, centre_vert, 'green', "Vert avec Barycentre")
        # afficher_resultat(seg_blue, centre_bleu, 'blue', "Bleu avec Barycentre")
        
        # plt.show()

        # Vérifie si toutes les paires de barycentres adjacentes sont détectées
        return ((adjacence_jaune_vert and adjacence_rouge_jaune) and (adjacence_vert_bleu and adjacence_jaune_vert) and (adjacence_bleu_rouge and adjacence_vert_bleu) and (adjacence_rouge_jaune and adjacence_bleu_rouge))
