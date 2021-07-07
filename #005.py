#005
'改变图像分辨率'
from PIL import Image
import os
filepath = r'C:\Users\MAC\Documents\GitHub\python\pictures'
def change_image(filepath):
    for imglist in os.listdir(filepath):
        imgpath = os.path.join(filepath,imglist)
        img = Image.open(imgpath)

        img_change = img.resize((1136,640))
        w,h = img_change.size
        
        #img_change.show()
        img_change.save('new'+imglist.split('.')[0]+'.jpg')

        print('new image size', imglist, ' is : %s x %s' % (w,h))
change_image(filepath)
