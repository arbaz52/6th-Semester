# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 10:02:04 2019

@author: Shark
"""


import cv2
import numpy

global image
global filter_
filter_ = [[2,2,2], [2,1,2], [2,2,2]]
global brush_range
brush_range = 3


frame_name = "original image"

image = cv2.imread("../picture.jpg", 0)
cv2.imshow(frame_name, image)

def mouse_callback_handler(event, x, y, flags, param):
    print(event, flags, param[y][x], x, y)
    
cv2.setMouseCallback(frame_name, mouse_callback_handler, image)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()