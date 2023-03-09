import glob

from PIL import Image

frames = []
images = sorted(glob.glob("/Users/ken/Desktop/MP/Large/data/20230225_161206/*.png"))

for image in images:
    new_frame = Image.open(image)
    frames.append(new_frame)

frames[0].save('jpg_to_gif.gif',
    format='GIF',
    append_images=frames[1:],
    save_all=True,
    duration=500,
    loop=0)