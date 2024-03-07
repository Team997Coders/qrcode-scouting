from qreader import QReader
import qreader
import qrtools
def getData(image):
    data = qreader.decodeQR(image)
    return data