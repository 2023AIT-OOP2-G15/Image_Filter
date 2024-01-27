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
    if type(pixels[0,0]) == int:
        img = Image.new("RGB",(rows,cols),((0,0,0)))
        for y in range(rows):
            for x in range(cols):
                if pixels[y,x] == 255:
                    img.putpixel((y,x),(255,230,230))
                else:
                    img.putpixel((y,x),(25,0,0))
    else:
        #print("通過しました")
        for y in range(rows):
            for x in range(cols):

                if len(pixels[0,0]) != 3:
                    alpha,r,g,b = pixels[y,x]
                else:
                    r,g,b = pixels[y,x]
                r = r+50
                if r>255:
                    r = 255
                    pixels[y,x] = r,g,b
    
    return img
        