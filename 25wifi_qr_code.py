
import qrcode

##Wifi Link
wifi_type = "WPA"
wifi_ssid = "AK47"
wifi_password = "Nepal@2080"
ifi = f"WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(wifi)
type(img)
img.save("wifi.png")