import qrcode

# Generate a QR code
data = input("Enter data to be encoded in the QR Code: ") 
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
image = qr.make_image(fill_color="black", back_color="white")
image.save("qrcode.png")