import webbrowser
import virtualassistant as va
import datetime
import os
import random

# Setting default browser to Chrome
chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser(chrome_path))


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        va.speak("Good Morning Sir!")
    elif (hour >= 12 and hour < 18):
        va.speak("Good Afternoon Sir!")
    else:
        va.speak("Good Evening Sir!")

    asstname = "Jarvis 1 point o"
    va.speak("I am " + asstname)


def openWebsite(site):
    webbrowser.open(site)


def start():
    def clear(): return os.system('cls')

    wishMe()
    clear()

    first = True
    questions = ["Is there anything else I can help you with today?",
                 "Will that be all sir?", "How else can I be of assistence sir?"]

    while True:

        if first:
            va.speak("How can I help you today?")
            first = False

        else:
            va.speak(random.choice(questions))

        query = (va.takeCommand()).lower()

        if 'calculator' in query:
            va.speak("Opening calculator")
            openWebsite("https://muniahmed.github.io/calculator/")

        elif 'youtube' in query:
            va.speak("Going to YouTube")

            openWebsite("https://youtube.com")

        elif 'inspire' in query or "quote" in query:
            va.speak("Booting up motivation protocal sir")
            openWebsite("https://muniahmed.github.io/random-quote-machine/")

        elif 'github' in query or 'code' in query:
            va.speak("Opening Github. Happy hacking sir")
            openWebsite("https://github.com")

        elif 'who made you' in query:
            va.speak("Taking you to the master's other works. Enjoy sir")
            openWebsite("https://muniahmed.github.io/cv/")

        elif 'quit' in query or "rest" in query:
            va.speak("Very well sir, take care now")
            exit()

        else:
            va.speak("I'm sorry sir, I did not quite catch that")
