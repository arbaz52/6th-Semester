# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:57:12 2019

@author: Shark
"""
import cv2
import numpy as np
np.random.seed(123)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras import backend as K
K.set_image_dim_ordering('th') 

#for now, it works for only 28x28 images
def predict(model, imagepath):
    img = cv2.imread(imagepath, 0)
    img = np.expand_dims(img, 0)
    imgs = np.array([img])
    imgs = imgs.astype("float32")
    imgs /= 255
    pred = model.predict(imgs)[0]
    #print(pred)
    i = 0
    m = pred[i]
    for j, v in enumerate(pred):
        if v > m:
            m = v
            i = j
    return i
    
    

#loading the presaved model
model = Sequential()

model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(1,28,28))) 
model.add(Convolution2D(32, 3, 3, activation='relu')) 
model.add(MaxPooling2D(pool_size=(2,2))) 
model.add(Dropout(0.25))
model.add(Flatten()) 
model.add(Dense(128, activation='relu')) 
model.add(Dropout(0.5)) 
model.add(Dense(10, activation='softmax'))
# 6. Compile model 
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])



#loading
model.load_weights("model_state")

#prediction
print(predict(model, "images/zero.png"))
print(predict(model, "images/one.png"))
print(predict(model, "images/two.png"))
print(predict(model, "images/three.png"))
print(predict(model, "images/four.png"))
print(predict(model, "images/five.png"))
print(predict(model, "images/six.png"))
print(predict(model, "images/seven.png"))
print(predict(model, "images/eight.png"))
print(predict(model, "images/nine.png"))

    
