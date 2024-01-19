import cv2
import os
import json

def Vintage(image):
    filename = image[:-4]
    current_directory = os.path.dirname(os.path.abspath(__file__))
    upload_directory_path = os.path.join(current_directory, '../../static/uploads')
    # 画像の読み込み
    img = cv2.imread(upload_directory_path+'/'+image)
    rows,cols,channel = img.shape
    for y in range(rows):
        for x in range(cols):

            b,g,r = img[y,x]
            b = b+0
            g = g+51
            r = r+106
            if b>255:
                b = 255
            if g>255 :
                g = 255
            if r> 255:
                r = 255
            
            img[y,x] = b,g,r

    adjust_image = cv2.convertScaleAbs(img,alpha=1.0,beta=-50)
    return adjust_image