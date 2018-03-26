# Pi² Face Recognition

Fonctionne avec Anaconda (spyder) et python 3.6 SOUS LINUX/UBUNTU 16.04

## Le projet Pi²:

Face Recognition program for InMoov

Pi² Project ESILV 2017-2018 Team 28

Made by Martin Jérémy, Guillaume Thomas, Mézouar Chloé and Ekhteraei Aria.

Our project is for the humanoïd InMoov Robot, we had to implement a face recognition that is able to 
recognize around 50 differents persons and able to ask if there is an unknown person who wants to be add.
     

## Prérequis :

* Python 3.6
* OpenCV 3.3.0
* Dlib (dernière version)
* face recognition ( plus d'info -> https://github.com/ageitgey/face_recognition )

## Installation : 


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
if needed :
```sh
❯ pip3 install easygui
```
# La Reconnaissance

Il y a 3 versions de cette reconnaissance faciale :
* 1-Reconnait toutes les personnes qui sont présentes face caméra par rapport à un dataset déja existant.
* 2-Reconnait seulement la personne qui se trouve au plus proche de la caméra (ça évite de reconnaitre les personnes qui ne font que passer).
* 3-Exactement comme la version 2, mais qui à maintenant la fonctionnalité d'enregistrer, si elle le souhaite, une personne inconnue en direct 

Pour ce qui est de trouver un visage ou une autre partie du corps utilisez OpenCV -> go google. 

Pour plus d'information n'hésitez pas à suivre les liens que j'ai laissé ;)

N'oubliez pas de préciser le path de votre dataset sinon vous aurez des erreurs, assurez vous aussi d'avoir vos drivers de caméra à jour et actifs.

# Les à améliorer connus

* Si personne n'est reconnu au moment de l'ajout, le programme freeze
* Si vous rajoutez manuellement des personnes dans le dataset, le programme ne démarre plus

