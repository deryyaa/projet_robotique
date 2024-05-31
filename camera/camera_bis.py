import cv2 as cv
from matplotlib.pyplot import *
import numpy
import math
import imageio
import sys

def detecter_balise(img_path):
    pass

def coloriage_pixel_pile(image,shape,seuil,valeur,pile,i,j):
   image[j][i] = valeur
   voisins = [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
   for pixel in voisins:
        (k,l) = pixel
        if k>=0 and k<shape[1] and l>=0 and l<shape[0]:
            if image[l][k]>seuil:
                image[l][k] = valeur
                pile.append(pixel)

if __name__ == "__main__":

    img_path = r"C:\Users\nutella\Documents\LICENCE 2\S2\PROJET DE DEV\projet_robotique\pattern.jpg"
    detecter_balise(img_path)

    img = cv.resize(cv.imread(img_path, 1),(200,200))

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
    

   

