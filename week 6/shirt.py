import sys
import os.path
from os import path
from PIL import Image, ImageOps

#we can get the ext using splittext 
file_read = os.path.splitext(sys.argv[1])
file_write = os.path.splitext(sys.argv[2])

#if the user does not specify exactly two command-line arguments,
if len(sys.argv) < 3:
    sys.exit("too few command line arguments")

elif len(sys.argv) > 3:
    sys.exit("too many command line arguments")

#if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively
elif file_read[1] != ".jpg" and file_read[1] != ".jpeg" and file_read[1] != ".png":
    sys.exit("Invalid output")

#if the specified input does not exist.
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")

#if the input’s name does not have the same extension as the output’s name
elif file_read[1] != file_write[1]:
        sys.exit("Input and output have different extensions")

else:
#you have to open both pic not only one - Open the input with Image.open
    shirt = Image.open("shirt.png")
    user_image = Image.open(sys.argv[1])

#get the size of the picture & resize and crop the input with ImageOps.fit
    resized_image = ImageOps.fit(user_image, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

#using default values for method, bleed, and centering, overlay the shirt with Image.paste
    resized_image.paste(shirt, box=None, mask=shirt)

#and save the result with Image.save in the arvg 2 for output
    resized_image.save(sys.argv[2])



