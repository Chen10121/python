#000
'修改头像'
from PIL import Image, ImageDraw, ImageFont
imgpath = 'C:/Users/MAC/Documents/GitHub/python/hask.jpg'
fontpath = r'C:\Windows\Fonts\bahnschrift.ttf'
def image_add_number(num):
    img = Image.open(imgpath)
    w,h = img.size
    drawfont = ImageFont.truetype(fontpath,100)
    ImageDraw.Draw(img).text((w*0.75,h*0.08),str(num),font = drawfont,fill = 'red')
    img.show()
image_add_number(4)