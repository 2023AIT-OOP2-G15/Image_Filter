import cv2
import os
import json
from PIL import Image, ImageFilter

def Vintage(path):
    # 画像の読み込み
    img = Image.open(path)
    rows,cols = img.size
    pixels = img.load()
    for y in range(rows):
        for x in range(cols):

            if len(pixels[0,0]) != 3:
                alpha,r,g,b = pixels[y,x]
            else:
                r,g,b = pixels[y,x]
            b = b-50
            g = g+1
            r = r+56
            if b>255:
                b = 255
            if g>255 :
                g = 255
            if r> 255:
                r = 255
            
            pixels[y,x] = r,g,b

    #adjust_image = cv2.convertScaleAbs(pixels,alpha=1.0,beta=-50)
    return img