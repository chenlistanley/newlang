import PIL.Image as Image
import os
IMAGES_PATH = 'C:/Users/stanley/Downloads/100/'
IMAGES_FORMAT = ['.jpg', '.JPG']
IMAGE_SIZE = 256
IMAGE_ROW = 2
IMAGE_COLUMN = 2
IMAGE_SAVE_PATH = 'C:/Users/stanley/Downloads/100.jpg'

def test():
    image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if os.path.splitext(name)[1] == item]

    if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
        raise ValueError("合成图片的参数和要求的数量不能匹配！")

    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))

    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize((IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH)

def test2():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE))

    from_image=Image.open(IMAGES_PATH + "1.jpg").resize((IMAGE_SIZE, IMAGE_SIZE * 2),Image.ANTIALIAS)
    to_image.paste(from_image, (0 * IMAGE_SIZE, 0 * IMAGE_SIZE))

    from_image=Image.open(IMAGES_PATH + "2.jpg").resize((IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
    to_image.paste(from_image, (1 * IMAGE_SIZE,  0 * IMAGE_SIZE))

    from_image=Image.open(IMAGES_PATH + "3.jpg").resize((IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
    to_image.paste(from_image, (1 * IMAGE_SIZE, 1 * IMAGE_SIZE))

    to_image.save(IMAGE_SAVE_PATH)

test2()