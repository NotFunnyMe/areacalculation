from PIL import Image
import random

im = Image.open("")# enter img path
rgb_im = im.convert('RGB')
count_in = 0
count_pun = 0
count = 0
while(count<=100000):
    x= random.randint(0,2480)
    y= random.randint(0,2375)
    z = 0
    r, g, b = rgb_im.getpixel((x, y))
    if(r==60):
        count_in+=1
        count+=1
    else:
        if(r==80):
            count_pun+=1
            count+=1

area_pun=(count_pun/count_in)*3287623
print(area_pun)
