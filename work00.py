from PIL import Image, ImageDraw, ImageFont
import random

msgNum = str(random.randint(1, 99))
Img_dir = 'Source\\testPhoto.jpg'
Save_dir = 'Source\\testPhoto01.jpg'


def add_num(img_dir, num, save_dir):
    # Read image
    im = Image.open(img_dir)
    w, h = im.size
    w_draw = 0.9 * w
    h_draw = 0.1 * h
    # Draw image
    font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 80)
    draw = ImageDraw.Draw(im)
    draw.text((w_draw, h_draw), num, font=font, fill=(255, 33, 33))
    # Save image
    im.save(save_dir, 'png')


add_num(Img_dir, msgNum, Save_dir)
