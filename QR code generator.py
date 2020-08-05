import pyqrcode
import time
import png
import pathlib
from pyqrcode import QRCode
a=input("Enter the required qr data : ")
data = a
img=pyqrcode.create(data)
img.png("myfirst",scale=10)
print("The QR code is saved in location "+str(pathlib.Path().absolute()))
time.sleep(3)
