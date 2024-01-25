from PIL import Image

def convert_to_grayscale(image_path):
    
    image = Image.open(image_path)

    grayscale_image = image.convert("L")

    return grayscale_image

#processed_image = convert_to_grayscale()