from PIL import Image
import numpy as np

def convert_to_Sepia(image_path='temporary.png'):
    # セピア色のカスタムRGB値
    sepia_rgb = (107, 74, 43)

    # 画像を読み込んでRGBAに変換
    img = Image.open(image_path).convert("RGBA")
    np_img = np.array(img)

    # グレースケールに変換
    gray = np.dot(np_img[..., :3], [0.2989, 0.5870, 0.1140])

    # セピア基調の処理
    sepia_base = gray / gray.max()
    sepia_img = np.zeros(np_img.shape)
    for i in range(3):
        sepia_img[..., i] = sepia_base * sepia_rgb[i]

    # クリップ処理
    sepia_img += 50  
    sepia_img = np.clip(sepia_img, 0, 255)
    sepia_img[..., 3] = np_img[..., 3]

    # 画像オブジェクトに変換して返す
    return Image.fromarray(sepia_img.astype('uint8'))

processed_image = convert_to_Sepia()