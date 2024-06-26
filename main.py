import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import time
from audioBook import readbook
from sendmessage import swm


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
    a = True
    if 'ok good bye' in text:
        a = False
    while a:
        run_alexa()


# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('Listening....')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 command = command.replace('alexa', '')
#                 print(command)
#     except:
#         pass
#     return command


def run_alexa():
    with sr.Microphone() as source:
        print('Listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
    if 'play' in command:
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        talk('playing'+song)
        print('playing....')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M :%p')
        talk('current time is'+time)
    elif 'who is ' in command:
        try:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except:
            person = command.replace('who is', '')
            pywhatkit.search(person)
    elif 'what is ' in command:
        try:
            thing = command.replace('what is', '')
            infomation = wikipedia.summary(thing, 1)
            print(infomation)
            talk(infomation)
        except:
            thing = command.replace('what is', '')
            pywhatkit.search(thing)
    elif 'which is ' in command:
        try:
            information = pywhatkit.info(command, lines=4)
            print(information)
            talk(information)
        except:
            pywhatkit.search(command)
    elif 'are you single' in command:
        talk('I have a relationship with wifi')
    elif 'joke' in command:
        jok = pyjokes.get_joke()
        talk(jok)
        print(jok)
    elif 'read book' in command:
        readbook()
    elif 'good bye' in command:
        talk('ok good bye')
    elif 'send whatsapp message' in command:
        swm()
    else:
        talk('please say it a again')


run_alexa()
