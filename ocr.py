#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:55:41 2019

@author: eric lu
"""

import pytesseract
from PIL import Image

# open image
image = Image.open('string.png')
code = pytesseract.image_to_string(image, lang='chi_tra')
print(code)