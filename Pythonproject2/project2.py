import qrcode
img = qrcode.make ('Gaurav Sunar')
type(img)
#qrcode.image.pil.PilImage
img.save("Gaurav.png")

