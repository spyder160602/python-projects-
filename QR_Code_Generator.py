import qrcode

data = "'spyder160602' Search me on Github !"
img = qrcode.make(data)
img.save("C:\\Users\\Moksh\\Desktop\\qr.png")  # Corrected path with double backslashes
