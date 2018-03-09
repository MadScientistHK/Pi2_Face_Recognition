# Pi2 Face Recognition

Fonctionne avec Anaconda (spyder) et python 3.6 SOUS LINUX/UBUNTU 16.04

## Prérequis :
---
* Python 3.6
* OpenCV 3.3.0
* Dlib (dernière version)
* face recognition ( plus d'info -> https://github.com/ageitgey/face_recognition )

## Installation : 
---

### Step n°1 OpenCV 3.3.0 : 
```sh
❯ pip3 install opencv-python
```
### Step n°2 Dlib : 

Dlib n'a pas de prérequis particulier mais je vous conseille ces 3 librairies :  
```sh
❯ pip install numpy
❯ pip install scipy
❯ pip install scikit-image
```
Pour installer dlib :
```sh
❯ pip install dlib
```
En cas de besoin : https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/
### Step n°3 Face Recognition : 
```sh
❯ pip3 install face_recognition
```
# La Reconnaissance

Il y a actuellement 2 versions, la première qui reconnait toutes les qui sont présentes face caméra, la deuxième reconnait seulement la personne qui se trouve au plus proche de la caméra (ça évite de reconnaitre les mauvaises personnes)

Pour ce qui est de trouver un visage ou une autre partie du corps utilisez OpenCV -> go google. 

Pour plus d'information n'hésitez pas à suivre les liens que j'ai laissé ;)

N'oubliez pas de préciser le path de votre dataset sinon vous aurez des erreurs, assurez vous aussi d'avoir vos drivers de caméra à jour et actifs.
