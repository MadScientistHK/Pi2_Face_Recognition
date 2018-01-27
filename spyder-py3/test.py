# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:09:40 2017

@author: Jeremy
"""
import cv2
import os

font = cv2.FONT_HERSHEY_SIMPLEX
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
i=0
compteur=0
list_face = os.listdir('Pi2/tmp_dataset')
i = len(list_face)
name = input('Votre nom : ')
freq = int(input('saut de frame = '))


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
        for (x, y, w, h) in faces:
            #DEBUG RECTANGLE     
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (200, 180, 0), 3)
            
            if compteur%freq==0:
                crop_face=cv2.flip(frame[y:y+h,x:x+w],1)
                cv2.imwrite('Pi2/tmp_dataset/'+name+'_{:>05}.jpg'.format(i),crop_face)
                i+=1

    # Display the resulting frame
        frame=cv2.flip(frame,1)
        cv2.putText(frame,str(i), (50, 50), font, 0.8, (100, 0, 255), 2)
        cv2.imshow('Video', frame)
        compteur += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()