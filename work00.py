from PIL import Image, ImageDraw, ImageFont
import random

msgNum = str(random.randint(1, 99))

# Read image
im = Image.open('Source\\testPhoto.jpg')
w, h = im.size
wDraw = 0.9 * w
hDraw = 0.01 * w

# Draw image
font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 80)
draw = ImageDraw.Draw(im)
draw.text((wDraw, hDraw), msgNum, font=font, fill=(255, 33, 33))

# Save image
im.save('Source\\testPhoto01.jpg', 'png')
