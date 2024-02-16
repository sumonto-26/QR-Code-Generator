import qrcode

qr = qrcode.QRCode(
    version = 3,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 2
    )
qr.add_data("Sumonto")
qr.make(fit = True)

img = qr.make_image(fill_color = "lightgreen", back_color = "black")
img.save("mycode.png")
