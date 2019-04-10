import math
import numpy
    
def down_sample_1d(image, new_image_width):
    image_width = len(image)
    if image_width <= new_image_width:
        print("Invalid arguments")
        return -1
    
    new_image = []
    #getting ratio of how many pixels to skip
    ratio = image_width/new_image_width
    ratio = round(ratio)
    index = 0
    while index < image_width and len(new_image) < new_image_width:
        new_image.append(image[index])
        #skipping pixels
        for i in range(ratio):
            index += 1
    """
    while len(new_image) < new_image_width:
        #missing = 1
        missing = new_image_width - len(new_image)
        new_image.append(image[image_width-missing])
    """
    return new_image


def down_sample_2d(image, new_image_width, new_image_height):
    image_height = len(image)
    image_width = len(image[image_height-1])
    
    if image_height <= new_image_height or image_width <= new_image_width:
        print("Invalid arguments!")
        return -1
    
    new_image = []
    

    ratio_height = round(image_height/new_image_height)
    index = 0
    while index < image_height and len(new_image) < new_image_height:
        row = down_sample_1d(image[index], new_image_width)
        if row == -1:
            return row
        
        new_image.append(row)
        
        #skipping rows
        for i in range(ratio_height):
            index += 1
    
    return numpy.asarray(new_image)
        
            
    
def up_sample_1d(image, new_image_width):
    image_width = len(image)
    if image_width >= new_image_width:
        print("Invalid arguments")
        return -1
    
    new_image = []
    ratio = round(new_image_width/image_width)
    for i in range(image_width):
        for j in range(ratio):
            if len(new_image) >= new_image_width:
                break
            new_image.append(image[i])
    
    
    while len(new_image) < new_image_width:
        #missing = 1
        missing = new_image_width - len(new_image)
        new_image.append(image[image_width-missing])
        
        
    return new_image
        
    
    
def up_sample_2d(image, new_image_width, new_image_height):
    image_height = len(image)
    image_width = len(image[image_height - 1])
    if image_width >= new_image_width or image_height >= new_image_height:
        print("Invalid arguments")
        return -1
    
    
    new_image = []
    ratio_height = round(new_image_height / image_height)
    
    for i in range(image_height):
        for j in range(ratio_height):
            if len(new_image) >= new_image_height:
                break
            row = up_sample_1d(image[i], new_image_width)
            new_image.append(row)
            
            
    
    while len(new_image) < new_image_height:
        #missing = 1
        missing = new_image_height - len(new_image)
        row = up_sample_1d(image[image_height-missing], new_image_width)
        new_image.append(row)
    
    return new_image
        

    

    
"""
image = [1,2,3,4,5,6,7,8,9,10]
for i in range(2, len(image)):
    print(down_sample_1d(image, i))
    
    
image = [[1,2,3,4,5]
         , [4,5,6,7,8]
         , [2,3,4,5,6]
         , [9,8,7,6,4]]
new_image = down_sample_2d(image, 2, 3)
print("DOWN SAMPLED 2d: ")
for i in new_image:
    print(i)
print()
    
new_image = up_sample_2d(new_image, 5, 4)
print("UP SAMPLED 2d: ")
for i in new_image:
    print(i)
print()

image = [1,2,3]
print("UP SAMPLE 1d")
print(up_sample_1d(image, 5))
print()

image = [
    [1,2,3]
    ,[4,5,6]
    ,[7,8,9]
    ]
new_image = up_sample_2d(image, 4, 4)
for i in range(len(new_image)):
    print(new_image[i])
    
new_image = down_sample_2d(new_image, 3, 3)
for i in range(len(new_image)):
    print(new_image[i])
    
"""
