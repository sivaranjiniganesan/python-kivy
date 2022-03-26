from kivy.uix.image import AsyncImage 
import kivy
from pygame import mixer 
from kivy.uix.label import Label 
from kivy.app import App   
from kivy.uix.widget import Widget
from kivy.config import Config 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput  
import pytesseract
from gtts import gTTS
import os 

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
img_text = pytesseract.image_to_string("C:\\Users\\sivar\\OneDrive\\Pictures\\Screenshots\\python.png")

print(img_text)

  



# defining the App class 
class MyLabelApp(App): 
    def build(self): 
        # label display the text on screen  
        lbl = Label(text =img_text)
        language = 'en'
  

        myobj = gTTS(text=img_text, lang=language, slow=False) 
          

        myobj.save("welcome.mp3") 
          
        mixer.init()
        mixer.music.load("welcome.mp3")
        #mixer.music.play()
        return lbl 
  
# creating the object 
label = MyLabelApp() 
# run the window 
label.run()


