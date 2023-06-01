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

# URLs to Study OCR :
https://pyimagesearch.com/2020/09/07/ocr-a-document-form-or-invoice-with-tesseract-opencv-and-python/
https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/
https://pyimagesearch.com/start-here/#working_with_video

=========================================================================================
