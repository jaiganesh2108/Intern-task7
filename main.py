from PIL import Image
import os

def resize(im, new_width):
    width, height = im.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = im.resize((new_width,new_height))
    return resized_image

files = os.listdir("assets")
extensions = ['jpg','png','jpeg']
for file in files:
    ext = file.split('.')[-1]
    if ext in extensions:
        im = Image.open('assets/'+file)
        im_resized = resize(im, 600)
        new_dir = 'resized_images'
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
        file = f'{new_dir}/{file}.jpg'
        im_resized.save(file, 'png', quality=100)