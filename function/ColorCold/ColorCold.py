import cv2
import os
from PIL import Image, ImageFilter

#import json
#ファイルのパスが引数になるからそのファイルを加工して保存する
#返り値が渡されるように変更
#アップロードされた画像が複数の場合
#uploadフォルダに存在するファイルの数を取得→それぞれのファイルの名前を取得→加工して保存
def ColorCold(path):
    #output = []
    #file_list = Image.open(path)
    #file_list = os.listdir(path='static/preview')
    #for i in range(0,len(file_list)):
        #print(file_list[i])
    #image = file_list
        #filename = image[:-4]
    #current_directory = os.path.dirname(os.path.abspath(__file__))
    #upload_directory_path = os.path.join(current_directory, '../../static/uploads')

        # 画像の読み込み
    #img = cv2.imread(path)#upload_directory_path+'/'+image)
    #rows,cols,channel = img.shape
    img = Image.open(path)
    rows,cols = img.size
    pixels = img.load()
    for y in range(rows):
        for x in range(cols):

            r,g,b = pixels[y,x]
            b = b+100
            if b>255:
                b = 255
            pixels[y,x] = r,g,b
        #if True:
        #    cv2.imshow('Vintage Effect', img)
        #    cv2.waitKey(0)
        #    cv2.destroyAllWindows()
    
        #print(len(output))
    
    return img