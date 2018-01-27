import cv2
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
name = input('Votre nom : ')
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
        for (x, y, w, h) in faces:
            crop_face=cv2.flip(frame[y:y+h,x:x+w],1)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('Pi2/tmp_dataset/'+name+'.jpg',crop_face)
                break   
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()