from PIL import Image
import os

Set_pic_size = (640, 1136)
Img_Dir = 'Source\\Image\\'


# 输入要改变的分辨率,二元数组,待改变的图片文件路径,列表形式,将图片修改后保存在当前目录下
def change_img_size(img_size_new, img_dir):
    # read img
    img_name = os.listdir(Img_Dir)
    for i in range(len(img_name)):
        __img = Image.open(img_dir + img_name[i])
        w, h = __img.size
        __changed_img = __img.transform(img_size_new, Image.QUAD, (0, 0, 0, h, w, h, w, 0))
        __changed_img.save(img_dir + img_name[i].split('.')[0] + 'copy'+'.jpg')
    return 0


change_img_size(Set_pic_size, Img_Dir)
