# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:41:48 2019

@author: Shark
"""

import image_filtering
import image_sampling
import contrast_stretching

from PIL import Image
import numpy

from matplotlib import pyplot as plotter


def display_image(image_array):
    temp_image = Image.fromarray(image_array)
    temp_image.show()
    
        
def invert_image(image_array):
    new_image_array = []
    for i in range(len(image_array)):
        new_image_row = []
        for j in range(len(image_array[0])):
            new_image_row.append( 255 - image_array[i][j] )
        new_image_array.append(new_image_row)
    return numpy.asarray(new_image_array)

image = Image.open("picture.jpg").convert("L")
image_array = numpy.array(image)

#scaling down image for use
image_array = image_sampling.down_sample_2d(image_array, len(image_array[0])/5, len(image_array)/5)

display_image(image_array)
inverted_image_array = invert_image(image_array)

display_image(inverted_image_array)

contrast_stretched_image_array = contrast_stretching.constrast_stretching_2d(400, image_array)
display_image(contrast_stretched_image_array)
filter_5_5 = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]

filter_3_3 = [[1,1,1], [1,1,1], [1,1,1]]
filtered_image_array = image_filtering.filter_image(image_array, filter_5_5)
display_image(filtered_image_array)
hor_filter = [[1,0,-1], [1,0,-1], [1,0,-1]]
ver_filter = [[1,1,1], [0,0,0], [-1,-1,-1]]

hor_filtered_image_array = image_filtering.filter_image(image_array, hor_filter, 1)
display_image(hor_filtered_image_array)
ver_filtered_image_array = image_filtering.filter_image(image_array, ver_filter, 1)
display_image(ver_filtered_image_array)

grad_image_array = image_filtering.grad_image(hor_filtered_image_array, ver_filtered_image_array)
display_image(grad_image_array)


pixel_count = contrast_stretching.get_pixels_array_with_count(image_array)
plotter.plot(pixel_count)