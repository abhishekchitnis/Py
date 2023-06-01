=========================================================================================
# Using PyTesseract from PyPi 
import pytesseract
from PIL import Image

# Using Tesseract Installed Locally for OCR
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract'

# Perform Text Extraction # PyPi PyTesseract
text = pytesseract.image_to_string(Image.open('OCREx.png'))

# Displaying Extraracted Text
print(text)

=========================================================================================

# Using PDFMiner from PyPi 
from pdfminer.high_level import extract_text

# Perform Text Extraction
text = extract_text("un.pdf")

# Displaying Extraracted Text
print(text)

=========================================================================================
