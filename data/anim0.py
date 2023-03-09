import cv2
import math
import numpy as np
import colorsys
import os
from datetime import datetime
import matplotlib.pyplot as plt

def now_str(str_format='%Y%m%d%H%M'): #image name yyyy/mm/dd
    return datetime.now().strftime(str_format)

result_dir = '/Users/ken/Desktop/MP/Large/data/' + now_str(str_format='%Y%m%d_%H%M%S')
os.makedirs(result_dir, exist_ok=True)

# 円描画
def drawCircle(angle, x, y, rt, s):
    rgb = colorsys.hsv_to_rgb(angle/(math.pi*2), s, 1)
    cv2.circle(image, (x, y), rt, \
        (int(rgb[2]*255),int(rgb[1]*255),int(rgb[0]*255)), \
        -1,lineType=cv2.LINE_AA)

tail = np.zeros((576, 576, 3), np.uint8)

width, height = 260, 260
image = np.zeros((height, width, 3), np.uint8)
cx = width // 2
cy = height // 2
r,rt = 68, 60
div = 32
sz = 94
for i in range(0, div):
    image.fill(255)

    angle = (i - 2) * math.pi * 2 / div
    x = int(r * math.cos(angle) + cx)
    y = int(r * math.sin(angle) + cy)
    drawCircle(angle, x, y, rt, 0.3)

    angle = (i - 1) * math.pi * 2 / div
    x = int(r * math.cos(angle) + cx)
    y = int(r * math.sin(angle) + cy)
    drawCircle(angle, x, y, rt, 0.6)

    angle = i * math.pi * 2 / div
    x = int(r * math.cos(angle) + cx)
    y = int(r * math.sin(angle) + cy)
    drawCircle(angle, x, y, rt, 1.0)

    # 画像出力
    # cv2.imwrite('image/img%02d.png' % (i), image)
    png_path = os.path.join(result_dir, "{0}.png".format(i))
    plt.savefig(png_path)
    plt.close()