from qrcode import QRCode

qr = QRCode()
qr.add_data('https://www.python.org/')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("D:\\repo\\Python-Lessons\\python_qr.jpeg")