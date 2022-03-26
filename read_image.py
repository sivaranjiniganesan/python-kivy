import pytesseract
from pygame import mixer 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string("C:\\Users\\sivar\\OneDrive\\Pictures\\Screenshots\\react.png"))


# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
mytext = 'Welcome to geeksforgeeks!'
  
# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed
print(mytext)
#myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
##myobj.save("welcome.mp3")
##
##mixer.init()
##mixer.music.load("welcome.mp3")
##mixer.music.play()
  
# Playing the converted file 
#os.system("mpg321 welcome.mp3") 


##import cv2
##import numpy as np
##
##image = cv2.imread('C:\\Users\\sivar\\OneDrive\\Pictures\\Screenshots\\react.png')
##gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
##sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
##sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
##thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
##
##kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
##close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
##result = 255 - close
##
##
##cv2.imshow('result', result)
##cv2.waitKey()
