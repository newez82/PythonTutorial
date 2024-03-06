"""
    Image modification
"""

import os

from PIL import Image, ImageFilter

SIZE_300 = (300, 300)
SIZE_700 = (700, 700)
# image1 = Image.open("Exericse\\pillow_library_for_image_manipulation\\shiba1.jpg")

# display image on screen
# image1.show()

print("Get Current Directory: ", os.getcwd(), "\n")
# Change directory
os.chdir("Exericse\\pillow_library_for_image_manipulation")
print("Get Changed Directory: ", os.getcwd(), "\n")

# save image in png format
# image1.save("Exericse\\pillow_library_for_image_manipulation\\shiba1.png")
for file in os.listdir("."):
    if file.endswith(".jpg"):
        img = Image.open(file)
        file_name, file_ext = os.path.splitext(file)
        print(f"filename: {file_name} file extension: {file_ext}")
        img.save(f"pngs/{file_name}.png")
        # resize each file
        img.thumbnail(SIZE_300)
        img.save(f"300px/{file_name}_300{file_ext}")
        img.thumbnail(SIZE_700)
        img.save(f"700px/{file_name}_700{file_ext}")

# rotate image
image1 = Image.open("shiba1.jpg")
image1.rotate(90).save("shiba1_mod_rotate_90.jpg")

# convert to black and white color, go to pillow documentation for mode
image1.convert(mode="L").save("shiba1_mod_black_and_white.jpg")

# blur an image
# GaussianBlur default of radius 2
image1.filter(ImageFilter.GaussianBlur()).save("shiba1_mod_blur.jpg")
