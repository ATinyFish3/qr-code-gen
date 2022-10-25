# Create QR code images

# import modules

import qrcode

# inputs
data = "https://atinyfish3.github.io/files/CURRICULUM-VITAE.html"
img_name = 'CV-QR.png'

# create qr data
qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)

# create image

img = qr.make_image(fill='black', back_colour='white')
img.save(img_name)
