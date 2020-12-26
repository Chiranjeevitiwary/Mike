import speech_recognition as sr
from requests import get
import pyttsx3, datetime
import webbrowser
import wikipedia
import os
import cv2
import random

engine = pyttsx3.init("sapi5")
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=3, phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")
    except Exception as e:
        speak("Say That again please!")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hi i am Mike. Please tell me how can i help you?")

if __name__== "__main__":
    wish()
    while True:

        query = takecommand().lower()
        if "open notepad" in query:
             npath = "C:\\WINDOWS\\system32\\notepad.exe"
             os.startfile(npath)

        elif "open command" in query:
             cpath = "C:\\WINDOWS\\system32\\cmd.exe"
             os.startfile(cpath)

        elif "open chrome" in query:
             chpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
             os.startfile(chpath)

        elif "open camera" in query:
             cap = cv2.VideoCapture(0)
             while True:
                 ret, img = cap.read()
                 cv2.imshow('webcam', img)
                 k = cv2.waitKey(50)
                 if k ==27:
                     break
             cap.release()
             cv2.destroyAllWindows()

        elif "play music" in query:
            music = "F:\\Video Songs\\Video Songs\\"
            songs = os.listdir(music)
            rd = random.choice(songs)
            os.startfile(os.path.join(music, rd))

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your ip address is {ip}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikpedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Sir! What should i search on google?")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

