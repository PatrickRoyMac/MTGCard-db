import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

path =r"E:\MTG-Carddb\MTGCard-db\vampire.jpg"

#image processing
img = cv2.imread(path)
img = cv2.resize(img, None, fx=0.7, fy=0.7)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 2)

config = "--psm 3"
text = pytesseract.image_to_string(adaptive_threshold,config=config)
print(text)

cv2.imshow("Img",adaptive_threshold)
cv2.waitKey(0)
