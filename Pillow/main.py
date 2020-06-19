from PIL import Image

img = Image.open("leo.jpg")
print(img.size)
print(img.format)

img.show()