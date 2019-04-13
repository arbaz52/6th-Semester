# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:17:29 2019

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



#loading images for training

training_data_folderpath = "C:/Users/Shark/Desktop/Training Data"
i = 0
x_arbaz = []
x_not_arbaz = []
#one hot representation right away
y_arbaz = []
y_not_arbaz = []

ration = 2
new_height = int(192/ration)
new_width = int(146/ration)
while True:
    path = training_data_folderpath + "/arbaz/" + "face_" + str(i) + ".jpg"
    if not isfile(path):
        break
    
    file = cv2.imread(path, 0)
    
    file = down_sample_2d(file, new_width, new_height)
    file = np.expand_dims(file, 0)
    
    one_hot = np_utils.to_categorical(0, 2)
    x_arbaz.append(file)
    y_arbaz.append(one_hot)
    
    i += 1
print("images read: {}".format(i))

i = 0
while True:
    path = training_data_folderpath + "/not arbaz/" + "face_" + str(i) + ".jpg"
    if not isfile(path):
        break
    
    file = cv2.imread(path, 0)
    file = down_sample_2d(file, new_width, new_height)
    file = np.expand_dims(file, 0)
    
    
    one_hot = np_utils.to_categorical(1, 2)
    x_not_arbaz.append(file)
    y_not_arbaz.append(one_hot)
    
    i += 1
print("images read: {}".format(i))

x_arbaz = np.array(x_arbaz)
x_not_arbaz = np.array(x_not_arbaz)


#formatting data
x_arbaz = x_arbaz.astype("float32")
x_not_arbaz = x_not_arbaz.astype("float32")
x_arbaz /= 255
x_not_arbaz /= 255

y_arbaz = np.array(y_arbaz)
y_not_arbaz = np.array(y_not_arbaz)

#training data
x_train = []
y_train = []
for i in range(700):
    x_train.append(x_arbaz[i])
    y_train.append(y_arbaz[i])
for i in range(150):
    x_train.append(x_not_arbaz[i])
    y_train.append(y_not_arbaz[i])

x_train = np.array(x_train)
y_train = np.array(y_train)

#testing data
x_test = []
y_test = []
for i in range(700, len(x_arbaz)):
    x_test.append(x_arbaz[i])
    y_test.append(y_arbaz[i])
for i in range(150, len(x_not_arbaz)):
    x_test.append(x_not_arbaz[i])
    y_test.append(y_not_arbaz[i])

x_train = np.array(x_train)
y_train = np.array(y_train)

x_test = np.array(x_test)
y_test = np.array(y_test)

# 7. Fit model on training data 
model.fit(x_train, y_train, batch_size=32, nb_epoch=10, verbose=1)
# 8. Evaluate model on test data 
score = model.evaluate(x_test, y_test, verbose=1)
model.save("model_state")