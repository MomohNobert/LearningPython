from PIL import Image

img = Image.open("leo.jpg")
# print(img.size)
# print(img.format)

# 4 parameters. 1st 2, x and y co-ordinates of left corner.
area = (100, 100, 300, 375)
cropped_img = img.crop(area)

# img.show()
cropped_img.show()