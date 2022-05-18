import pytesseract
import cv2

image = cv2.imread('img/HKID/new_2.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = get_grayscale(image)

# Traditionsal Chinese text image to string
#print(pytesseract.image_to_string(Image.open('img/HKID/new_2.jpg'), lang='chi_tra'))#for full name
print(pytesseract.image_to_string(gray, lang='chi_tra'))#for HKID

cv2.imshow('img', gray)
cv2.waitKey(0)