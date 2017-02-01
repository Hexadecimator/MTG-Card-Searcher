# MTG-Card-Searcher
Program to convert the names of magic the gathering cards that are held under a kinect device to a text string and then use that string to search the magic card's price on TCGPlayer.com

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
