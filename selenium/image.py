from PIL import Image
from pytesseract import image_to_string
im=Image.open('2.gif')
imgry = im.convert('L')
imgry.show()
threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
# out为2值化结果
out.show()
print(image_to_string(out, config='-psm 7'))