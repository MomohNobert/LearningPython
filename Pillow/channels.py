from PIL import Image

img = Image.open('afro.jpg')
r, g, b = img.split()

# g.show()

new_img = Image.merge('RGB', (g,r,b))
new_img.show()