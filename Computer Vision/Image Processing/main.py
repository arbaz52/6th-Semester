# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:02:32 2019

@author: Shark
"""
import cv2
frame = "frame 1"
def mouse_drawing(event, x, y, flags, params):
    print(image[y][x])
        
global image
image = cv2.imread("../Quiz/picture.jpg", 0)

cv2.imshow(frame, image)
cv2.setMouseCallback(frame, mouse_drawing)
#opencv2 for 64bit machine 
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()