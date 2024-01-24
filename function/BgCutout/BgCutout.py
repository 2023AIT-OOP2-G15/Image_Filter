import cv2
import numpy as np
from PIL import Image

def convert_to_BgCutout(image_path='temporary.png'):
    # 画像を開く
    image = Image.open(image_path)

    # OpenCV用に画像を変換（PillowからOpenCVへの変換）
    cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # グレースケール変換
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

    # 2値化
    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    # 輪郭を検出
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 背景を透明にした画像を作成
    result_image = np.ones_like(cv_image) * 255

    # 各輪郭を描画
    cv2.drawContours(result_image, contours, -1, (0, 0, 0), thickness=cv2.FILLED)

    # OpenCVからPillowへの変換
    result_image_pil = Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))

    # 結果画像を返す
    return result_image_pil

# 関数を呼び出し
result_image = convert_to_BgCutout()

# 結果を保存（例として、適当なファイル名で保存しています）
result_image.save('output_bg_cutout_image_opencv.png')