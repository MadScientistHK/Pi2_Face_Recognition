#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:11:47 2017

@author: jeremy
"""

import face_recognition
import cv2
import os

def knownFaces():
    list_face = os.listdir('Pi2/tmp_dataset')
    i = len(list_face)
    known_faces = [i]
    index = 0
    for face in list_face:
        faceLoad = face_recognition.load_image_file("Pi2/tmp_dataset/"+face)
        known_faces.append(face_recognition.face_encodings(faceLoad)[0])
        index = index+1
    print(known_faces)
    return known_faces

knownFaces()