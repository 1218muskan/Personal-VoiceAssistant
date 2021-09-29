# importing the dependencies
import speech_recognition as sr  # for recognition of human speech
import pyttsx3  # for text to speech conversion
import datetime
import wikipedia # makes it easy to access and parse data from Wikipedia
import webbrowser # it provides a high-level interface to allow displaying Web-based documents to users.
import os
import time
import subprocess # A subprocess in Python is a task that a python script delegates to the Operative system (OS).
# from ecapture import ecapture as ec
import wolframalpha  # Wolfram Alpha is an API which can compute expert-level answers using Wolfram’s algorithms, knowledgebase and AI technology.
import requests  # its the de facto standard for making HTTP requests in Python
import pyaudio



# configuring engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

# function for text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()


# for greetings depending upon current time
def wishMe():
    hour = datetime.datetime.now().hour

    if hour >=0 and hour < 12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")

    elif hour >=12 and hour <18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")

    else:
        speak("Hello, Good Evening")
        print("Hello, Good Evening")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')  #indian english
            print(f"User said: {statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"

        return statement




print("Loading your personal voice Assistant -- VoiceAssist 1.0")
speak("Loading your Personal voice assistant VoiceAssist 1.0")
wishMe()


if __name__ == '__main__':

    while True:
        speak("Tell me how can I help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "goodbye" in statement or "bye" in statement or "stop" in statement or "quiet" in statement:
            speak('your personal assistant voiceAssist is shutting down,Good bye')
            print('Your Personal Assistant VoiceAssist is shutting down,Good bye')
            break

        if 'wikipedia' in statement:
            speak('Searching Wikipedia')
            print("Searching Wikipedia...")

            speak("What do you want to search on wikipedia ?")
            print("What do you want to search on wikipedia ?")
            wiki_srch = takeCommand()

            try:
                results = wikipedia.summary(wiki_srch, sentences=3)

            except Exception:
                speak("Couldn't Find!")
                print("Couldn't Find!")

            else:          # execute if no exception
                speak("According to Wikipedia ")
                print(results)
                speak(results)

        elif 'open youtube' in statement or 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is opened")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is opened")
            time.sleep(5)     #sleep for 5 sec

        elif 'open gmail' in statement or 'open mail' in statement:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Google mail opened")
            time.sleep(5)

        elif 'weather' in statement:
            api_key = ""  # Get your api key from Open Weather website
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("Tell the city name")
            print("City ?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)    # making an api call
            x = response.json()

            if x['cod'] != "404":
                y = x["main"]
                current_temp = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_desc = z[0]["description"]

                speak(" Temperature in kelvin unit is " +
                      str(current_temp) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_desc))

                print(" Temperature in kelvin unit = " +
                      str(current_temp) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_desc))

            else:
                speak("City not found!")
                print("City not Found")
                break


        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement or 'about yourself' in statement:

            print("I am Muskan friend VoiceAssist 1.0 . I am programmed to do minor tasks. You can also ask me computational or geographical questions")

            speak("""I am Muskan friend VoiceAssist version 1 point O your persoanl assistant. I am programmed to do minor tasks like
                opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather
                in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!""")

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was build by Muskan Gupta")
            print("I was build by Muskan Gupta")

        elif 'open stack overflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from Times of India, Happy reading")
            time.sleep(6)

        # elif 'camera' in statement or "take a photo" in statement or "capture the moment" in statement:
        #     ec.capture(0,"robo camera","img.jpg")   # index, window name , image name

        elif 'search' in statement:
            statement = statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions. What question do you want to ask?')
            question = takeCommand()
            app_id = "" # paste here your app id from WolframAlpha website
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)


        elif "log off" in statement or "sign out" in statement or "shut down" in statement or "turn off computer" in statement:
            speak("OK , Your pc will log off in 15 seconds. Make sure you exit from all applications")
            subprocess.call(["shutdown","/l"])


time.sleep(3)





