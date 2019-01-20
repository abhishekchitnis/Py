import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR/tesseract'
text = pytesseract.image_to_string(Image.open('OCREx.png'))
print(text)
