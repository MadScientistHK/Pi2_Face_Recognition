import face_recognition
import os

def knownFaces():
    list_face = os.listdir('Pi2/tmp_dataset')
    known_faces = []
    for face in list_face:
        #encode each face of the folder
        faceLoad = face_recognition.load_image_file("Pi2/tmp_dataset/"+face)
        known_faces.append(face_recognition.face_encodings(faceLoad)[0])
    return known_faces

knownFaces()