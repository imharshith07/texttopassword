#speech to text
from gtts import gTTS #importing gtts
import os
#enter the text you want to convert to speech
mytext = input("Enter text:")

launguage = 'en'#specifieng the input launguage

output = gTTS(text=mytext,lang=launguage,slow='false')

#naming the file which is converted to speech with mp3 format
str = input("filename")+'.mp3'

output.save(str)#saving the file

#opening the mp3 file to play converted speech in windows.
#In linux it won't works,you can play it from your directory manually
os.system('start '+str)
