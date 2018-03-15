import face_recognition
import cv2
import os
#import sys
from generate_encoding import knownFaces
from math import sqrt
import easygui
#from pymsgbox import *
import threading
from queue import Queue
#from util import takeFace,bigFace,choice

def takeFace(face_locations,small_frame,known_faces,res):   
    #name = input('Votre nom : ')
    name = easygui.enterbox('Votre nom : ','Face recognition')
    for (top, right, bottom, left) in face_locations:  
        crop_face=cv2.flip(small_frame[top:bottom,left:right],1)
    cv2.imwrite('Pi2/tmp_dataset/'+name+'.jpg',crop_face)
    known_faces = knownFaces()
    res.put(known_faces)
    return

def bigFace(small_frame):
    faces = face_recognition.face_locations(small_frame)
    max=0
    bigface = []
    j=0
    index=0
    for (top, right, bottom, left) in faces:
        if(sqrt((right-left)*(right-left)+(top-bottom)*(top-bottom)) > max):
            max=sqrt((right-left)*(right-left)+(top-bottom)*(top-bottom))
            index=j
        j=j+1
    if(faces == []):return []
    else:
        bigface.append(faces[index])
    return bigface


def choice(face_locations,small_frame,known_faces,res):
    if(easygui.ynbox('Do you want to be in the dataset ?', 'Face recognition', ('Yeah', 'Hell no !')) == True):
        takeFace(face_locations,small_frame,known_faces,res)
    else:
        res.put(known_faces)
        return         
        
def fr():
    #HOG : Histogram of Oriented Gradients <- Model/Method
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    #get all the encoded faces from generate_encoding
    #known_faces = knownFaces()
    ret = video_capture.set(3,1920)
    ret = video_capture.set(4,1080)
    res = Queue()
    known_faces = knownFaces()
    #print(known_faces)
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    timet = 0
    process_this_frame = True
    while True:
        
        # Grab a single frame of video
        
        ret, frame = video_capture.read()

        
        
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
        # Only process every other frame of video to save time
        if process_this_frame:
           
            # Find all the faces and face encodings in the current frame of video
            #face_locations = face_recognition.face_locations(small_frame)
            face_locations = bigFace(small_frame)
            face_encodings = face_recognition.face_encodings(small_frame, face_locations)
            face_names = []
            thread = threading.Thread(target=choice,args=(face_locations,small_frame,known_faces,res,))
            
            
            
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                match = face_recognition.compare_faces(known_faces,face_encoding)
                #add 1234 because of the .jpeg extension
                name = "Unknown1234"
                list_face = os.listdir('Pi2/tmp_dataset')
                for face in list_face:
                    for i in range(len(match)):
                        if match[i]:
                            name = list_face[i]
                #remove the .jpeg from face's name then put the text
                face_names.append(name[:-4])
                
                
                if(face_names[0] == "Unknown"):
                    if(timet > 100):
                        if(thread.is_alive() == False):
                            thread.start()
                            known_faces = res.get()
                        timet = 0
                    timet=timet+1
                    
                    
        process_this_frame = not process_this_frame
        # Display the results
        
        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (102, 102, 0), 2)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (102, 102, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            
        # Display the resulting image
        cv2.imshow('Video', frame)
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release handle to the webcam

    video_capture.release()
    cv2.destroyAllWindows()     
    
    
    
fr()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    