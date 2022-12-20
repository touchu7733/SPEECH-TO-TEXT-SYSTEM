import sys
import voice_handler as vh
import speech_recognition as sr
# import email_handler as eh
from time import sleep


engine = vh.init_engine()
voice = vh.get_voice(engine)
vh.speak("Hello, do you want to add groceries or send the list?", voice, engine)
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk,i am listening...")
    audio = r.record(source, duration=5)

choice = r.recognize_google(audio, language='en-US')
print(choice)

if "i want to add" in str(choice).lower():
    vh.speak("Let me know what you want to add?", voice, engine)
    while True:
        vh.speak("aha", voice, engine)
        addition = vh.get_audio()
        if "done" in str(addition).lower():
            break
        print(addition)
        f = open("shooping_list.txt", "a")
        f.write(addition + "\n")
        f.close()
# elif "send" in choice:
#     vh.speak("Sending the current list to your email", voice, engine)
#     with open ("shooping_list.txt", "r") as file:
#         shopping_list = file.read()
#         eh.email_alert('Shopping list', shopping_list)
else:
    vh.speak("Please restart me. I am still not that complicated", voice, engine)
    sys.exit()