# Convert PDF to Image # Using PyPi PyMuPDF 
import fitz
pdf = fitz.open('image.pdf')
page = pdf.load_page(0)
pix = page.get_pixmap() #(dpi=300)
pix.pil_save("img2.jpg") 

# Using Tesseract Installed Locally for OCR
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Using OpenCV for Processing Image
import cv2
# Grayscale, Gaussian blur, Otsu's ThresHold
image = cv2.imread('musho.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph Open to Remove Noise and Invert Image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Perform Text Extraction # PyPi PyTesseract
data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')

# Displaying Extraracted Text
print(data)
