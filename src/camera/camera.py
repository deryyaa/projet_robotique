import cv2 as cv
from matplotlib.pyplot import *
import numpy 
import math
import imageio
import sys


def detecter_balise(img_path):
    pass

def verifier_adjacence(barycentre1, barycentre2, seuil):
    distance = math.sqrt((barycentre2[0] - barycentre1[0])**2 + (barycentre2[1] - barycentre1[1])**2)
    print(distance)
    return round(distance) < seuil
def isBalise(image):
    if __name__ == "__main__":

        img = cv.resize(cv.imread(image, 1),(200,200))

        hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
        
        hue,sat,val = cv.split(hsv)
        
        #Segmentation balise

        #rouge 
        lower_red1 = np.array([0, 190, 0], dtype=np.uint8)
        upper_red1 = np.array([15, 255, 255], dtype=np.uint8)
        seg_red1 = cv.inRange(hsv, lower_red1, upper_red1)

        lower_red2 = np.array([340/2, 190, 0], dtype=np.uint8)
        upper_red2 = np.array([360/2, 255, 255], dtype=np.uint8)
        seg_red2 = cv.inRange(hsv, lower_red2, upper_red2)

        # Combiner les deux segments
        seg_red = cv.bitwise_or(seg_red1, seg_red2)
        median_seg_red = cv.medianBlur(seg_red,9)
        # Calculer les moments de l'image segmentée
        moments = cv.moments(median_seg_red)

        # Calculer les coordonnées du barycentre
        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
        else:
            cX, cY = 0, 0

        # Afficher la segmentation et le barycentre
        figure(figsize=(4, 4))
        imshow(median_seg_red, cmap=cm.gray)
        scatter(cX, cY, color='red', s=50, marker='x')  # Marquer le barycentre
        title("Rouge avec Barycentre")
        centre_rouge = (cX,cY)
        
        

        #jaune
        lower = numpy.array([36/2,180,0],dtype=numpy.uint8)
        upper = numpy.array([60/2,255,255],dtype=numpy.uint8)
        seg = cv.inRange(hsv,lower,upper)
        median_seg = cv.medianBlur(seg,9)
        
        # Calculer les moments de l'image segmentée
        moments = cv.moments(median_seg)

        # Calculer les coordonnées du barycentre
        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
        else:
            cX, cY = 0, 0

        # Afficher la segmentation et le barycentre
        figure(figsize=(4, 4))
        imshow(median_seg, cmap=cm.gray)
        scatter(cX, cY, color='red', s=50, marker='x')  # Marquer le barycentre
        title("Jaune avec Barycentre")
        centre_jaune = (cX,cY)

        #verte
        lower = numpy.array([70/2,0,0],dtype=numpy.uint8)
        upper = numpy.array([180/2,255,255],dtype=numpy.uint8)
        seg = cv.inRange(hsv,lower,upper)
        median_seg = cv.medianBlur(seg,9)
        # Calculer les moments de l'image segmentée
        moments = cv.moments(median_seg)

        # Calculer les coordonnées du barycentre
        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
        else:
            cX, cY = 0, 0

        # Afficher la segmentation et le barycentre
        figure(figsize=(4, 4))
        imshow(median_seg, cmap=cm.gray)
        scatter(cX, cY, color='red', s=50, marker='x')  # Marquer le barycentre
        title("Vert avec Barycentre")
        centre_vert = (cX,cY)

        
        #bleu 
        lower = numpy.array([190/2,190,0],dtype=numpy.uint8)
        upper = numpy.array([255/2,255,255],dtype=numpy.uint8)
        seg = cv.inRange(hsv,lower,upper)
        median_seg = cv.medianBlur(seg,9)
        # Calculer les moments de l'image segmentée
        moments = cv.moments(median_seg)

        # Calculer les coordonnées du barycentre
        if moments['m00'] != 0:
            cX = int(moments['m10'] / moments['m00'])
            cY = int(moments['m01'] / moments['m00'])
        else:
            cX, cY = 0, 0

        # Afficher la segmentation et le barycentre
        figure(figsize=(4, 4))
        imshow(median_seg, cmap=cm.gray)
        scatter(cX, cY, color='red', s=50, marker='x')  # Marquer le barycentre
        title("Bleu avec Barycentre")
        centre_bleu = (cX,cY)


        show()

        # Seuils de distance pour chaque paire de couleurs voisines
        seuil_jaune_vert = 71  # Seuil de distance entre jaune et vert
        seuil_vert_bleu = 64   # Seuil de distance entre vert et bleu
        seuil_bleu_rouge = 70  # Seuil de distance entre bleu et rouge
        seuil_rouge_jaune = 64 # Seuil de distance entre rouge et jaune

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

        if ((adjacence_jaune_vert and adjacence_rouge_jaune) and (adjacence_vert_bleu and adjacence_jaune_vert) and (adjacence_bleu_rouge and adjacence_vert_bleu) and (adjacence_rouge_jaune and adjacence_bleu_rouge)):

        