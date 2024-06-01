import cv2
import numpy as np

capture = cv2.VideoCapture("C:\\Users\\nutella\\Documents\\LICENCE 2\\S2\\PROJET DE DEV\\projet_robotique\\video.mp4")
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite("C:\\Users\\nutella\\Documents\\LICENCE 2\\S2\\PROJET DE DEV\\projet_robotique\\img_video\frame_{frameNr}.jpg", frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()