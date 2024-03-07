import qrcode_reader
from PIL import Image

qrcode = Image.open('qrcodeexample.png')


print(qrcode_reader.getData(qrcode))
