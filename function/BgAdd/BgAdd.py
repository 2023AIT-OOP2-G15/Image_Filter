from PIL import Image

def convert_to_BgAdd(input_image_path, background_image_path):
    
    foreground = Image.open(input_image_path)
    background = Image.open(background_image_path)

    background = background.resize(foreground.size, Image.Resampling.LANCZOS)

    background.paste(foreground, (0, 0), foreground)

    
    return background

#processed_image = convert_to_BgAdd()