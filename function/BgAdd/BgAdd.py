from PIL import Image

def convert_to_BgAdd(input_image_path, background_image_path,bg_color=(255, 255, 255)):
    
    # 前景画像と背景画像を読み込む
    foreground = Image.open(input_image_path)
    background = Image.open(background_image_path)

    # 前景画像をRGBAに変換
    foreground = foreground.convert("RGBA")

    # 前景画像の背景を透過させる
    datas = foreground.getdata()
    newData = []
    for item in datas:
        # 背景色に近い色を透明にする
        if item[0] == bg_color[0] and item[1] == bg_color[1] and item[2] == bg_color[2]:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    foreground.putdata(newData)

    # 背景画像を前景画像と同じサイズにリサイズ
    background = background.resize(foreground.size, Image.Resampling.LANCZOS)

    # 透過した前景画像を背景画像に重ねる
    background.paste(foreground, (0, 0), foreground)

    return background

#processed_image = convert_to_BgAdd()