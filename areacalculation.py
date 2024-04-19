import imageio
from PIL import Image
import numpy as np
import random

img = imageio.imread("pind.jpg")
count_pun = 0
count_id = 0
count = 0
while(count <= 10000):
    x = random.randint(0,2735)
    y = random.randint(0,2480)
    z = 0
    if (img[x][y][z] == 60):
        count_id += 1
        count = count+1
    else:
        if(img[x][y][z] == 80):
            count_pun += 1
            count = count+1

area_pun = (count_pun/count_id)*3287236
print(area_pun)