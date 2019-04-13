# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:27:48 2019

@author: Shark
"""

import cv2


drawing = False
point1 = ()
point2 = ()
def mouse_drawing(event, x, y, flags, params):
    global point1, point2, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        if drawing is False:
            drawing = True
            point1 = (x, y)
        else:
            drawing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            point2 = (x, y)

video_capture = cv2.VideoCapture(0)


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_drawing)

while True:
    _, frame = video_capture.read()
    
    if point1 and point2:
        cv2.rectangle(frame, point1, point2, (0, 255, 0))
        
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", gray_frame)
    
    
    key_pressed = cv2.waitKey(1) & 0xFF
    if key_pressed == ord("q"):
        break
    elif key_pressed == ord("c"):
        print("working")
    
    
cv2.destroyAllWindows()
