from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:\\Users\\Moksh\\Desktop\\qr.png")

result = decode(img)

print(result)
