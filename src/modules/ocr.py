import pytesseract
from pytesseract import Output

class OCR:
    def __init__(self):
        self.config = r'--oem 3 -l rus -c --tessdata-dir=/usr/local/share/tessdata/'
    
    def process(self, img):
        d = pytesseract.image_to_data(img, output_type=Output.DICT, config=self.config)
        return d