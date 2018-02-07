import numpy as np
import cv2
import requests
import pyttsx
import time
cap = cv2.VideoCapture(1)
address = 'http://172.16.192.148/ESPsmartHouse/ESPsmartHouse.php?face='
current_milli_time = lambda: int(round(time.time() * 1000))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
engine = pyttsx.init()
last_spoke_time = current_milli_time()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
    # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces = face_cascade.detectMultiScale(gray, 1.3, 3)
        
        if len(faces) > 0:
            #r = requests.get(address+'1')
            if((current_milli_time() - last_spoke_time) > 2000):
                print(faces[0][0])
                #engine.say('let me out')
	        #engine.runAndWait()
                last_spoke_time = current_milli_time()
                print("Talking")
        else:
	    pass
            #r = requests.get(address+'0')
       
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
     
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    # Display the resulting frame
        cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
