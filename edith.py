import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import pyaudio



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("How may I help You?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again Please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://google.com")
        elif 'open gmail' in query:
            webbrowser.open("https://gmail.com")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open edlantic' in query:
            webbrowser.open("https://mcs.edlantic.com")
        elif 'open school website' in query:
            webbrowser.open("https://modernconventschool.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open photoshop' in query:
            pspath = "C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (64 Bit)\\Photoshop.exe"
            os.startfile(pspath)
        elif 'open bluestacks' in query:
            bpath = "F:\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(bpath)
        elif 'open remote desktop' in query:
            rdpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome_proxy.exe"
            os.startfile(rdpath)
        elif 'open epic games' in query:
            egpath = "F:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(egpath)
        elif 'open edge' in query:
            epath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(epath)
        elif 'open pycharm' in query:
            ppath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.1\\bin\\pycharm64.exe"
            os.startfile(ppath)
        elif 'open visual studio' in query:
            vspath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(vspath)
        elif 'open excel' in query:
            mepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010"
            os.startfile(mepath)
        elif 'open powerpoint' in query:
            mppath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
            os.startfile(mppath)
        elif 'open word' in query:
            mwpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010"
            os.startfile(mwpath)
        elif 'open publisher' in query:
            mpupath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Publisher 2010"
            os.startfile(mpupath)
        elif 'open movies' in query:
            movies_dir = 'F:\\NEW MOVIES'
            os.startfile(movies_dir)
        elif 'search google for' in query:
            webbrowser.open("https://google.com/search?q=" + query)
        elif 'search youtube for' in query:
            webbrowser.open("https://youtube.com/search?q=" + query)
        elif 'weather' in query:
            webbrowser.open("https://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396")
        elif 'who made you' in query:
            speak("I am made by Aaryaman")
        elif 'can you detect ghost' in query:
            speak("Yes, that is what I am made for")
        elif 'who are you' in query:
            speak("I am Jarvis, Speed 250 mmegabits. I am made by Aaryaman")
        elif 'how are you' in query:
            speak("I am fine, Thank you for asking")
        elif 'I am also fine' in query:
            speak("Ok")
        elif 'please tell me about sports' in query:
            webbrowser.open("https://www.google.com/search?q=sports&oq=sports&aqs=chrome..69i57j0l6.1213j0j7&sourceid=chrome&ie=UTF-8jarvis.py")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 0")
        elif 'restart' in query:
            os.system("shutdown /r /t 0")
        elif "exit" in query:
            sys.exit()

