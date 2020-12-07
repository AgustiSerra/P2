from PIL import Image
import os, sys

#creates the variable path where is located the image
path = '/Users/agustiserra/Desktop/'
dirs = os.listdir( path )

#function that resizes the image
def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((400, 400), Image.ANTIALIAS)   #here we established the new size
            imResize.save(f + 'resizedImage.jpg', 'JPEG', quality = 90) #saves the new resized image
resize()
