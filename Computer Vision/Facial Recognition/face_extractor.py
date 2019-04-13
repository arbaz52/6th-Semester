# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:27:48 2019

@author: Shark
"""

import cv2


drawing = False
point1 = (233, 167)
point2 = (379, 359)

video_capture = cv2.VideoCapture(0)


cv2.namedWindow("Frame")

training_data_folderpath = "C:/Users/Shark/Desktop/Training Data/not arbaz/"
face_images_count = 0

while True:
    _, frame = video_capture.read()
    
    if point1 and point2:
        cv2.rectangle(frame, point1, point2, (0, 255, 0))
        
    #storing the gray_frame for easy training data
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", frame)
    
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord("q"):
        break
    elif key_pressed == ord("c"):
        #extracting the face
        face = gray_frame[point1[1]: point2[1], point1[0]: point2[0]]
        cv2.imshow("Face", face)
        cv2.imwrite(training_data_folderpath+"/face_"+str(face_images_count)+".jpg", face)
        face_images_count += 1
        print("working")
    
    
cv2.destroyAllWindows()
