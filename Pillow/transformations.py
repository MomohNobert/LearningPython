from PIL import Image

img = Image.open('samuel.jpg')
square_jackson = img.resize((250, 250))
flip_jackson = img.transpose(Image.FLIP_LEFT_RIGHT)
spin_jackson = img.transpose(Image.ROTATE_90)

# square_jackson.show()
# flip_jackson.show()
spin_jackson.show()

