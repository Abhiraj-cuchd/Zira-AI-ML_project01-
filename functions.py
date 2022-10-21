from config import engine
import datetime
import speech_recognition as sr
import smtplib


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    '''
    Takes microphone input from the user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)
        print("Pardon, say that again please...")
        return "none"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("abhirajghosh123@gmail.com", "mylock@123")
    server.sendmail('abhirajghosh123@gmail.com', to, content)
    server.close()