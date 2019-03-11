import math
import numpy
import contrast_stretching
def create_image():
    image = []
    for i in range(7):
        row = []
        for j in range(4):
            row.append(20)
        for j in range(4):
            row.append(165)
        image.append(row)
    return image

def filter_image(image, filter_, v = False):
    image_height = len(image)
    image_width = len(image[image_height - 1])
    new_image = []
    for i in range(image_height):
        row = []
        for j in range(image_width):
            row.append(image[i][j])
        new_image.append(row)
    
    for i in range(len(image)):
        for j in range(len(image[i])):
            #filtering
            filter_center_row = int(len(filter_)/2)
            filter_center_col = int(len(filter_[filter_center_row])/2)
            value = 0
            diviser = 0
            for k in range(len(filter_)):
                row_index = k - filter_center_row + i
                for l in range(len(filter_[k])):
                    col_index = l - filter_center_col + j
                    if row_index >= 0 and row_index < image_height and col_index >= 0 and col_index < image_width:
                        value += image[row_index][col_index] * filter_[k][l]
                        diviser += filter_[k][l]
            if v != False:
                new_image[i][j] = int(value/v)
            else:
                new_image[i][j] = int(value/diviser)
    return contrast_stretching.constrast_stretching_2d(255, new_image)

def grad_image(gx, gy):
    new_image = []
    for i in range(len(gx)):
        row = []
        for j in range(len(gx[i])):
            row.append(int(math.sqrt(math.pow(gx[i][j], 2) + math.pow(gy[i][j], 2))))
        new_image.append(row)
    return numpy.asarray(new_image, numpy.uint8)

def display_image(img):
    print()
    for row in img:
        print(row)

"""
img = create_image()
filter_ = [
    [1,1,2,1,1],
    [1,3,4,3,1],
    [2,4,8,4,2],
    [1,3,4,3,1],
    [1,1,2,1,1]]
filter_1 = [[1,1,1],[1,1,1],[1,1,1]]
hor_filter = [[1,0,-1], [1,0,-1], [1,0,-1]]
ver_filter = [[1,1,1], [0,0,0], [-1,-1,-1]]
display_image(img)

gx = filter_image(img, hor_filter, 1)
display_image(gx)
gy = filter_image(img, ver_filter, 1)
display_image(gy)

gimg = grad_image(gx, gy)
display_image(gimg)
"""
