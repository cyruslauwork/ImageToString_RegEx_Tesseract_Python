#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 10:33:13 2021

@leadAuthor: LAU Ka Pui, Cyrus, from HKDI

"""

import re
import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('img/HKID/new.jpg')

def get_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = get_grayscale(img)

#d = pytesseract.image_to_string(gray, lang='chi_tra')
d = pytesseract.image_to_data(gray, output_type=Output.DICT)

hkid_patterns = ['^(\s)..(\d\d\d\d\d\d)...$',
                '^(\s).(\d\d\d\d\d\d)...$',
                '^..(\d\d\d\d\d\d)$',
                '^.(\d\d\d\d\d\d)$',
                '^..(\d\d\d\d\d\d)...$',
                '^.(\d\d\d\d\d\d)...$']

#matching
n_hkid_patterns = len(hkid_patterns)
for p in range(n_hkid_patterns):
    n_boxes = len(d['text'])#'len()' is to count the number of elements 
    for i in range(n_boxes):
        if int(d['conf'][i]) > 30:
            if re.match(hkid_patterns[p], d['text'][i]):
	            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#printMatch
n_hkid_patterns = len(hkid_patterns)
for p in range(n_hkid_patterns):
    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 30:
            if re.match(hkid_patterns[p], d['text'][i]):
                hkid_number = d['text'][i]
            
#Check if there is wrong HKID number starting with "2"
hkid_wrong_patterns = ['^(\s)2(\d\d\d\d\d\d)...$',
                       '^2(\d\d\d\d\d\d)...$',
                       '^2(\d\d\d\d\d\d)$']
n_wrong_patterns = len(hkid_wrong_patterns)
for i in range(n_wrong_patterns):
    if re.match(hkid_wrong_patterns[i], hkid_number):
        hkid_number = re.sub(r'\b2', 'Z', hkid_number)#syntax: re.sub(pattern, repl, string, count=0, flags=0)
print(hkid_number)

cv2.imshow('img', img)
cv2.waitKey(0)