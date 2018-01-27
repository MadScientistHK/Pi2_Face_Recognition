# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:09:40 2017

@author: Jeremy
"""
import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

def mvn(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        
        if(x<120):
            cv2.putText(frame,"mouvement droite", (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        if(x+w>520):
            cv2.putText(frame,"mouvement gauche", (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        if(y<100):
            cv2.putText(frame,"mouvement haut", (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        if(y+h>400):
            cv2.putText(frame,"mouvement bas", (x, y+h+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    
    
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()   
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
                )
    # Draw a rectangle around the faces
    
        xMax = 0
        yMax = 0
        wMax = 0
        hMax = 0
        for (x, y, w, h) in faces:
            mvn(frame)
    # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()