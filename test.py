from gtts import gTTS
import os

text = "I will speak this text"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")