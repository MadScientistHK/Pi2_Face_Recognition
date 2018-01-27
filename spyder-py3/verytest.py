#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:01:08 2017

@author: jeremy
"""

import face_recognition

# Load the jpg files into numpy arrays
moi_image = face_recognition.load_image_file("jeremy.jpg")
unknown_image = face_recognition.load_image_file("j3.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
moi_face_encoding = face_recognition.face_encodings(moi_image)[0]
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

known_faces = [
    moi_face_encoding,
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of me? {}".format(results[0]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))