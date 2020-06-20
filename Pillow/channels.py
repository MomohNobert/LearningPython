from PIL import Image

img = Image.open('luffy.jpg')
r, g, b, a = img.split()

g.show()
