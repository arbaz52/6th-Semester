# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:41:26 2019

@author: Shark
"""

from image_sampling import down_sample_2d
import numpy as np
import cv2
from os.path import isfile

np.random.seed(123)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras import backend as K
K.set_image_dim_ordering('th') 

model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(1,96, 73))) 
model.add(Convolution2D(32, 3, 3, activation='relu')) 
model.add(MaxPooling2D(pool_size=(2,2))) 
model.add(Dropout(0.25))
model.add(Flatten()) 
model.add(Dense(128, activation='relu')) 
model.add(Dropout(0.5)) 
#0: arbaz, 1: not arbaz
model.add(Dense(2, activation='softmax'))
# 6. Compile model 
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.load_weights("model_weights")

def predict(model, image):
    if image.shape != (96, 73):
        image = down_sample_2d(image, 73, 96)
    image = np.expand_dims(image, 0)
    print(image.shape)
    images = np.array([image])
    pred = model.predict(images)[0]
    if pred[0] > pred[1]:
        return "arbaz"
    else:
        return "not arbaz"
    
    
image = cv2.imread("C:/Users/Shark/Desktop/Training Data/not arbaz/face_100.jpg", 0)
predict(model, image)




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
        f = predict(model, face)
        print(f)
        cv2.imshow(f, face)
    
    
cv2.destroyAllWindows()
