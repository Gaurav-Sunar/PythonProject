
import qrcode
img = qrcode.make ('https:gapscponnect.com.au')
type(img)
#qrcode.image.pil.PilImage
img.save("Gaurav.png")


### create a QR code Generator that email to user
