from PIL import Image
from PIL import ImageFilter

img = Image.open('afro.jpg')

# converting to black and white
# bw_img = img.convert("L")

# bw_img.show()
blur = img.filter(ImageFilter.BLUR)
detail = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()