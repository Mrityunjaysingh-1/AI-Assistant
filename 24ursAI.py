# importing these libraries....
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio

print('Loading your AI personal assistant - 24urs')


# Setting up the speech engine:
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')


# define a function speak which converts text to speech,
# speak function takes the text as its argument,further initialize the engine.
def speak(text):
    engine.say(text)
    # runAndWait() function Blocks while processing all currently queued commands
    engine.runAndWait()


# function to greet the user
def wishMe():
    # here now().hour function abstract’s the hour from the current time.
    hour=datetime.datetime.now().hour
    # If the hour is greater than zero and less than 12,
    # the voice assistant wishes you with the message “Good Morning”.
    if hour>=0 and hour<12:
        speak("Hey,Good Morning")
        print("Hey,Good Morning")

    # If the hour is greater than 12 and less than 14,
    # the voice assistant wishes you with the following message “Good Afternoon”.
    elif hour>=12 and hour<14:
        speak("Hey,Good Afternoon")
        print("Hey,Good Afternoon")

    # If the hour is greater than 14 and less than 21
    # the voice assistant wishes you with the following message “Good Evening".
    elif hour>=14 and hour<21:
        speak("Hey,Good Evening")
        print("Hey,Good Evening")

    # Else it voices out the message “Good evening”
    else:
        speak("Hey,Good Night")
        print("Hey,Good Night")


# Define a function takecommand for the AI assistant to understand and to accept human language,
# The microphone captures the human speech and the recognizer recognizes the speech to give a response
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        #The exception handling is used to handle the exception during the run time error and,
        # the recognize_google function uses google audio to recognize speech.
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

speak("Loading your AI personal assistant 24urs")
wishMe()

# The main function starts from here,the commands given by the humans is stored in the variable statement.
if __name__=='__main__':

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        # If the following trigger words are there in the statement given by the users
        # it invokes the virtual assistant to speak the below following commands.
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant 24urs is shutting down,Good bye')
            print('your personal assistant 24urs is shutting down,Good bye')
            break


        # Skill 1 -Fetching data from Wikipedia:
        # The wikipedia.summary() function takes two arguments, the statement given by the user and
        # how many sentences from wikipedia is needed to be extracted is stored in a variable result.
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # Skill 2 -Accessing the Web Browsers — Google chrome , G-Mail and YouTube:
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        # Skill 3 -Predicting Weather:
        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        # Skill 4 -Predicting time:
        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        # about the assistant:
        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am 24urs version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')

        #about the developer
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Jay")
            print("I was built by Jay")

        # Skill 5 -Open Stackoverflow:
        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        # Skill 6 -To fetch latest news:
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        # Skill 7 -open camera:
        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        # Skill 8 -search anything:
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        # Skill 9 -ask anything:
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="PAK9YG-UJXGHQ6HHV"
            client = wolframalpha.Client('PAK9YG-UJXGHQ6HHV')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        # shutDown:
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(5)