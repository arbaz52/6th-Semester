# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:10:17 2019

@author: Shark
"""

import cv2


faceFile = "C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(faceFile)
videoCapture = cv2.VideoCapture(0)
facex = cv2.imread("face_0.png")

while True:
    ret, frame = videoCapture.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 
                                         scaleFactor = 1.1, 
                                         minNeighbors = 5, 
                                         minSize = (30, 30), 
                                         flags = cv2.CASCADE_SCALE_IMAGE)
    print("faces: ", len(faces))
    for i in range(len(faces)):
        (x, y, w, h) = faces[i]
        cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_img = gray[y: y+h+1, x: x+w+1]
        cv2.imwrite("face_" + str(i) + ".png", gray[y: y+h+1, x: x+w+1])
        if face_img == facex:
            cv2.putText(gray,"Arbaz", (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 255)
        else:
            cv2.putText(gray,"FFFAACCCEE", (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 255)
        
    cv2.imshow("frame", gray)
    cv2.imwrite("faces.png", gray)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



videoCapture.release()
cv2.destroyAllWindows()