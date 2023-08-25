from barcode import EAN13
from barcode.writer import ImageWriter
with open(r'Cod.png','wb') as arquivo:
    EAN13("1234567890123", writer=ImageWriter()).write(arquivo)