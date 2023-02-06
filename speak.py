from gtts import gTTS
import os

def speak(text):
    obj = gTTS(text=text, lang="en", slow=False)
    obj.save("tmp.mp3")
    os.system("mpg123 -q tmp.mp3")
