import qrcode
import random

# Data to be encoded
data = "https://priyanshurathod07.wordpress.com/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate random colors
fill_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
back_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Create an image from the QR Code instance
img = qr.make_image(
    fill_color=fill_color,  # Random fill color
    back_color=back_color,  # Random background color
)

# Save the image to a file
img.save("qrcode.png")