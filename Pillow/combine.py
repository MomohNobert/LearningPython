from PIL import Image

first_img = Image.open('marie.jpg')
second_img = Image.open('luffy.jpg')

area = ( 50, 50, 550,645)
print(second_img.size)
first_img.paste(second_img, area)

# second_img.show()