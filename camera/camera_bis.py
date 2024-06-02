import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt

def resize_img(img_path):
    img = cv.imread(img_path, 1)
    if img is None:
        print("Erreur: Impossible de lire l'image. Vérifiez le chemin du fichier.")
        return None
    else:
        return cv.resize(img, (200, 200))

def segmenter_couleur(hsv, lower, upper):
    seg = cv.inRange(hsv, lower, upper)
    median_seg = cv.medianBlur(seg, 9)
    moments = cv.moments(median_seg)
    if moments['m00'] != 0:
        cX = int(moments['m10'] / moments['m00'])
        cY = int(moments['m01'] / moments['m00'])
    else:
        cX, cY = 0, 0
    return median_seg, (cX, cY)

def afficher_resultat(image, barycentre, couleur, title):
    plt.figure(figsize=(4, 4))
    plt.imshow(image, cmap='gray')
    plt.scatter(barycentre[0], barycentre[1], color=couleur, s=50, marker='x')
    plt.title(title)

def verifier_adjacence(barycentre1, barycentre2, seuil):
    distance = math.sqrt((barycentre2[0] - barycentre1[0])**2 + (barycentre2[1] - barycentre1[1])**2)
    return round(distance) < seuil

if __name__ == "__main__":

    img_path = r"C:\Users\nutella\Documents\LICENCE 2\S2\PROJET DE DEV\projet_robotique\img_lamda.jpg"
    img = resize_img(img_path)
    
    if img is not None:
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        
        # Rouge
        lower_red1 = np.array([0, 190, 0], dtype=np.uint8)
        upper_red1 = np.array([15, 255, 255], dtype=np.uint8)
        seg_red1 = cv.inRange(hsv, lower_red1, upper_red1)
        lower_red2 = np.array([340/2, 190, 0], dtype=np.uint8)
        upper_red2 = np.array([360/2, 255, 255], dtype=np.uint8)
        seg_red2 = cv.inRange(hsv, lower_red2, upper_red2)

        seg_red = cv.bitwise_or(seg_red1, seg_red2)
        median_seg_red = cv.medianBlur(seg_red,9)
        moments = cv.moments(median_seg_red)

        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
        else:
            cX, cY = 0, 0
        
        centre_rouge = (cX,cY)

        # Jaune
        lower_yellow = np.array([36/2, 180, 0], dtype=np.uint8)
        upper_yellow = np.array([60/2, 255, 255], dtype=np.uint8)
        seg_yellow, centre_jaune = segmenter_couleur(hsv, lower_yellow, upper_yellow)
        
        # Vert
        lower_green = np.array([70/2, 0, 0], dtype=np.uint8)
        upper_green = np.array([180/2, 255, 255], dtype=np.uint8)
        seg_green, centre_vert = segmenter_couleur(hsv, lower_green, upper_green)
        
        # Bleu
        lower_blue = np.array([190/2, 190, 0], dtype=np.uint8)
        upper_blue = np.array([255/2, 255, 255], dtype=np.uint8)
        seg_blue, centre_bleu = segmenter_couleur(hsv, lower_blue, upper_blue)

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
        afficher_resultat(seg_red, centre_rouge, 'red', "Rouge avec Barycentre")
        afficher_resultat(seg_yellow, centre_jaune, 'yellow', "Jaune avec Barycentre")
        afficher_resultat(seg_green, centre_vert, 'green', "Vert avec Barycentre")
        afficher_resultat(seg_blue, centre_bleu, 'blue', "Bleu avec Barycentre")
        
        plt.show()