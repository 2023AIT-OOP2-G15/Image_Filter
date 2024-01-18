from PIL import Image, ImageFilter

def convert_to_gradation(image_path='temporary.png'):
    # 画像をロードする
    original_image = Image.open(image_path)

    # ガウシアンブラーを適用する
    blurred_image = original_image.filter(ImageFilter.GaussianBlur(5))

    # 加工した画像オブジェクトを返す
    return blurred_image

# 関数を使用する例（'temporary.png' を読み込んで加工）
processed_image = convert_to_gradation()