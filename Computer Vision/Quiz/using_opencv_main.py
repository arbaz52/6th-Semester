# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:43:30 2019

@author: Shark
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:41:48 2019

@author: Shark
"""

import image_filtering
import image_sampling
import contrast_stretching

import cv2
import numpy

from matplotlib import pyplot as plotter

global frame_name
frame_name = 'image displayer'
        
def invert_image(image_array):
    return 255 - image_array;


def mouse_callback_handler(event, x, y, flags, param):
    frame = param[0]
    image = param[1]
    print(event, flags, image[y][x], x, y)
    if event == 1 or (event == 0 and flags == 1):
        #
        
        image_width = len(image[0])
        image_height = len(image)
        filter_ = [[12,12,12],[12,1,12],[12,12,12]]
        diviser = 0
        filter_center_row = int(len(filter_)/2)
        filter_center_col = int(len(filter_[0])/2)
        for i in range(y-3, y+4):
            for j in range(x-3, x + 4):
                value = 0
                for k in range(len(filter_)):
                    row_index = k - filter_center_row + i
                    for l in range(len(filter_[k])):
                        col_index = l - filter_center_col + j
                        if row_index >= 0 and row_index < image_height and col_index >= 0 and col_index < image_width:
                            value += image[row_index][col_index] * filter_[k][l]
                            diviser += filter_[k][l]
                image[i][j] = int(value/diviser)
    cv2.imshow(frame, image)
    

frame_name = "original image"
#image = cv2.imread("picture.jpg", 0)
image = cv2.imread("Cameramantif.png", 0)
cv2.imshow("original image", image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, image))



#sampling down the image
frame_name = "down sampled image"
down_sampled_image = image_sampling.down_sample_2d(image, len(image[0])/3, len(image)/3)
cv2.imshow(frame_name, down_sampled_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, down_sampled_image))

#image = down_sampled_image


frame_name = "inverted image"
inverted_image = invert_image(image)
cv2.imshow(frame_name, inverted_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, inverted_image))


frame_name = "contrast stretched image"
contrast_strectched_image = contrast_stretching.constrast_stretching_2d(120, image)
cv2.imshow(frame_name, contrast_strectched_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, contrast_strectched_image))


frame_name = "blurred image"
filter = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
filtered_image = image_filtering.filter_image(image, filter)
cv2.imshow(frame_name, filtered_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, filtered_image))


frame_name = "horizontal filtered image"
hor_filter = [[1,0,-1], [1,0,-1], [1,0,-1]]
hor_filtered_image = image_filtering.filter_image(image, hor_filter, 1)
cv2.imshow(frame_name, hor_filtered_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, filtered_image))


frame_name = "vertical filtered image"
ver_filter = [[1,1,1],[0,0,0],[-1,-1,-1]]
ver_filtered_image = image_filtering.filter_image(image, ver_filter, 1)
cv2.imshow(frame_name, hor_filtered_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, ver_filtered_image))

frame_name = "gradient image"
grad_magnitude_image = image_filtering.grad_image(hor_filtered_image, ver_filtered_image)
cv2.imshow("gradient image", grad_magnitude_image)
cv2.setMouseCallback(frame_name, mouse_callback_handler, (frame_name, grad_magnitude_image))

#histogram
arr = contrast_stretching.get_pixels_array_with_count(image)
plotter.plot(arr)




cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()