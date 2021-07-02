from PIL import Image

# read img
img = Image.open('Source\\Image\\img01.jpg')
# img.show()
w, h = img.size
img_new = img.transform((400, 400), Image.QUAD, (0, 0, 0, h, w, h, w, 0))
img_new.show()