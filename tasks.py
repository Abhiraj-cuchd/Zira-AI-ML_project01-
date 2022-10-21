from functions import speak, sendEmail, takeCommand
import wikipedia
import webbrowser
import pywhatkit
import os
import datetime


def tasks(query):
    #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube, please wait")
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("opening google, please wait")
            webbrowser.open("google.com")
        
        elif 'open stack overflow' in query:
            speak("opening stackoverflow, please wait")
            webbrowser.open("https://stackoverflow.com")
        
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%I:%M:%p")
            speak(f"sir, The time is: {str_time}")

        elif 'open vs code' in query:
            speak("opening vs code.. please wait")
            code_path = "C:\\Users\\abhir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'send email' in query:
            try:
                speak("What should i say?..")
                content = takeCommand()
                to = "abhirajghosh26@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry, i am not able to send, please check net connection and try again")
        
        elif 'i love you' in query:
            speak("Are you single?")
            res = takeCommand().lower()
            if 'yes' in res:
                speak('I would love to! what is your name?')
                name = takeCommand().lower()
                speak(f"I love you too, {name}")
            
            elif 'no' in res:
                speak('You already have a girlfriend, you cheating on her')
                speak("Try me when you are single. Bye for now")

            #print("haha, i wish to do the same, but you already have a girlfriend.")
            
            
        elif 'play' in query:
            song  = query.replace('play','')
            speak('Playing' + song + "just a second..")
            pywhatkit.playonyt(song)
        
        elif 'whatsapp'in query:
            speak("What should i say?")
            content = takeCommand()
            pywhatkit.sendwhatmsg("+919101363971", content, 2,10)


            