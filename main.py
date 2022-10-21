from functions import  takeCommand, speak
import datetime
from tasks import tasks

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    
    else:
        speak("Good evening")
    
    speak("Zira here, How may i help you?")
    

wishMe()
while True:
    query = takeCommand().lower()
    tasks(query)

        





