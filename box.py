import cv2
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

sample = 'sample.png'

cmd = '/usr/local/Cellar/tesseract/4.0.0/bin/tesseract'
sample = cv2.imread('sample.png')
pytesseract.pytesseract.tesseract_cmd = cmd

text = pytesseract.image_to_string(sample)
print(text)

boxes = pytesseract.image_to_boxes(sample).split('\n')

h, w, _ = sample.shape
for b in boxes:
    b = b.split(' ')
    sample = cv2.rectangle(sample,(int(b[1]),h-int(b[2])),(int(b[3]),h-int(b[4])),(255,255,0),1)

cv2.imwrite('output.jpg', sample)
plt.imshow(sample)


