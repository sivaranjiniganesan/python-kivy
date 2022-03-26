     
import kivy       
from kivy.app import App     
from kivy.uix.widget import Widget  
from kivy.uix.textinput import TextInput    
from kivy.uix.boxlayout import BoxLayout   
from kivy.config import Config  
     

Config.set('graphics', 'resizable', True) 
  
# creating the root widget used in .kv file  
class BtnTextInput(BoxLayout): 
    pass
  
# class in which we are creating the Textinput and btn 
# in .kv file to be named main.kv  
class MainApp(App):  
    # defining build()  
    def build(self):  
        # returning the instance of root class 
        return BtnTextInput() 
  
# run function runs the whole program  
# i.e run() method which calls the target  
# function passed to the constructor. 
if __name__ == '__main__': 
    MainApp().run() 
