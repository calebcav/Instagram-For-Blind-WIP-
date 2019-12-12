import speech_recognition as sr
from gtts import gTTS
import os
import subprocess

def intro():

    Helen = gTTS(text = "Hello, my name is Helen. How may I help you today? ", lang="en", slow=False)
    Helen.save("hello.mp3")
    subprocess.call(["afplay", "hello.mp3"])


def speechToText():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        Helen = gTTS(text="Would you like to proceed?")
        Helen.save("talk.mp3")
        subprocess.call(["afplay", "talk.mp3"])
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            Helen = gTTS(text=f"Did you say, {text}?", lang="en", slow=False)
            print(text)
            Helen.save("talk.mp3")
            subprocess.call(["afplay", "talk.mp3"])
            return text
        except:
            Helen = gTTS(text="Sorry, I couldn't hear you", lang="en", slow=False)
            Helen.save("talk.mp3")
            subprocess.call(["afplay", "talk.mp3"])
            return False

