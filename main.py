from PIL import Image
import os

def resize(img,new_width):
    width,height = img.size
    ratio = height/width
    new_height = int(ratio*new_width)
    resized_image = img.resize((new_width,new_height))
    return resized_image

files = os.listdir("images")
extensions = ['jpg','jpeg','png','gif']
for file in files:
    ext = file.split(".")[-1]
    if ext in extensions:
        img = Image.open("images/" + file)
        img_resized = resize(img,300)
        file_path = f"images/{file}.jpeg"
        img_resized.save(file_path)