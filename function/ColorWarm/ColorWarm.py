import cv2
import os
import json
from PIL import Image, ImageFilter

def ColorWarm(path):
    
    #for i in range(len(file_list)):
    #filename = image[:-4]
    # 画像の読み込み
    img = Image.open(path)    
    rows,cols = img.size
    pixels = img.load()    
    for y in range(rows):
        for x in range(cols):

            r,g,b = pixels[y,x]
            r = r+100
            if r>255:
                r = 255
            pixels[y,x] = r,g,b
    
    return img
        