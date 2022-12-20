from ast import Return
import random
import speech_recognition as sr
import pyttsx3
from sympy import re

def init_engine():
    return pyttsx3.init()

def check_all_voices(engine):
    voices = engine.getProperty('voices')
    for voice in voices:
        print("Voice:")
        print(" - ID: %s" % voice.id)
        print(" - Name: %s" % voice.name)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)

def speak(text, voice, engine):
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 130) # Speed percent can go over 100
    engine.say(text)
    engine.runAndWait()

def get_voice(engine):
    voices = engine.getProperty('voices')
    # Windows voice check (for Mac first call check_all_voices)
    # and choose a proper voice that you like
    for voice in voices:
        if "Zira" in voice.name:
            desired_voice = voice
            break

    return desired_voice

def get_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.record(source, duration=5)

    said = r.recognize_google(audio, language='en-US')
    return said
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Talk,i am listening...")
    #     audio_text = r.listen(source)
    #     print("Time over, thanks")
    #     # print("Text: "+r.recognize_google(audio_text))
    #     # print("Text:"+r.recognize_google(audio_text, language = "te-IN"))
    #     word = r.recognize_google(audio_text)

    # return word