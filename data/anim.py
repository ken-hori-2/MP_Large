from PIL import Image
import glob
import pprint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

files = sorted(glob.glob('/Users/ken/Desktop/MP/Large/data/20230225_144212/*.png'))  
# pprint.pprint(files)
    
# images = list(map(lambda file : Image.open(file) , files))
# images[0].save('anime.gif', save_all=True, \
#     append_images=images[1:], optimize=True, duration=100 , loop=0)

# # plt.close()

fig = plt.figure()
ims = []

for i in range(500):
    # rand = np.random.randn(100) # 100個の乱数を作成
    
    # img = plt.plot(rand) # グラフを作成
    # plt.title("sample animation")
    # plt.ylim(-10,10)
 
    ims.append(files) # グラフを配列に追加
 
 

# 100枚のプロットを 100ms ごとに表示するアニメーション
ani = animation.ArtistAnimation(fig, ims, interval=100)
plt.show()