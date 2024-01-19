import cv2
import os
import json

def ColorWarm(path):
    output = []
    file_list = os.listdir(path=path)
    for i in range(len(file_list)):
    #filename = image[:-4]
        image = file_list[i]
        current_directory = os.path.dirname(os.path.abspath(__file__))
        upload_directory_path = os.path.join(current_directory, '../../static/uploads')

    # 画像の読み込み
        img = cv2.imread(upload_directory_path+'/'+image)
        rows,cols,channel = img.shape
        for y in range(rows):
            for x in range(cols):

                b,g,r = img[y,x]
                r = r+100
                if r>255:
                    r = 255
                img[y,x] = b,g,r
        output.append(img)
    return output
        