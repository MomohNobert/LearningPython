from PIL import Image
from PIL import ImageFilter

img = Image.open('afro.jpg')

# converting to black and white
# bw_img = img.convert("L")

# bw_img.show()
blur = img.filter(ImageFilter.BLUR)
blur.show()