# pip commands for all packages:
# pip install pytesseract
# pip install opencv-python
# pip install numpy
# pip install cython (if using tesser-ocr which is a newer version of pytesseract)
# 
# most of this code is found from the youtube video:
# How to recognize text from image with Python OpenCV OCR
# https://www.youtube.com/watch?v=83vFL6d57OI
#
# For tesseract, you need to install pytesseract and then go
# to the google tesseract repository and install the windows
# version of tesseract (MAKE SURE TO ADD IT TO PATH):
# https://github.com/UB-Mannheim/tesseract/wiki
#
# you also may need to install Cython which means you'll need the
# C++ compiler here (2015):
# http://landinghub.visualstudio.com/visual-cpp-build-tools 
#

import cv2
import numpy as np
from PIL import Image#, ImageEnhance, ImageFilter
import pytesseract
import webbrowser

def main():
    
    url = 'http://shop.tcgplayer.com/productcatalog/product/show?newSearch=false&ProductType=All&IsProductNameExact=false&ProductName='
    """
    TODO: SOURCE "img" WITH A KINECT IMAGE
     - use kinect to take an image the name of a magic card every 5 seconds
     - and then attempt to use OCR to read any text that it can from that name
     - use the string that is returned to search TCGPlayer.com for the price of all cards with that name
    """
    
    # Read image with opencv
    img = cv2.imread("TXT_IMG.png")   
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    # Apply dilation and erosion to remove some noise and write this new image to a file 
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite("removed_noise.png", img)
    # Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite("thresh.png", img)
    # Use tesseract to recognize the text from each image we generated and then print it
    print("Threshold: " + pytesseract.image_to_string(Image.open("thresh.png")))
    print("Removed Noise: " + pytesseract.image_to_string(Image.open("removed_noise.png")))
    print("Original Image: " + pytesseract.image_to_string(Image.open("TXT_IMG.png")))
    
    # Pack whatever string Tesseract came back with into a search TCGPlayer search URL
    search_string = pytesseract.image_to_string(Image.open("removed_noise.png"))
    # Then use this string to open a search of the text on TCG player
    # new = 2 means new browser tab is opened if possible
    # new = 1 means entire new browser window is opened if possible
    # new = 0 means the URL is opened in the currently active browser window
    webbrowser.open(url+search_string.replace(" ","%20"), new=2)



main()