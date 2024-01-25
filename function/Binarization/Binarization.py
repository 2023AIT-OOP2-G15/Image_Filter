from PIL import Image

def convert_to_Binarization(image_path='temporary.png', threshold_value=128):
    # 画像を開く
    image = Image.open(image_path)

    # モードを"L" (8-bit pixels, black and white) に変更
    image = image.convert("L")

    # 2値化を行う
    binarized_image = image.point(lambda p: p > threshold_value and 255)

    # 2値化された画像を返す
    return binarized_image

# 関数を呼び出し
result_image = convert_to_Binarization()

# 結果を保存（例として、適当なファイル名で保存しています）
result_image.save('output_binary_image.png')