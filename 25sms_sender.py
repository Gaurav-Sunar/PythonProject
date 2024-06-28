
import qrcode

##SMS
phone = "0420706798"
message = "Hello, how are you "
sms = f"SMSTO:{phone}:{message}"
img = qrcode.make(sms)
type(img)
img.save("sms.png")