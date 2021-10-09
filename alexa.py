# Created by Lalit Shirsath

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import json
import requests


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour<12):
        speak("Hii, Good morning, have a nice day")
        
    elif(hour<18):
        speak("Hii, Good afternoon")
    
    else:
        speak("Hii, Good night")
    
    speak("how may i help you ?")
        
# takes microphone input and return string
def takeCommand():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        query=r.recognize_google(audio)
        print("user said : ",query+"\n")
        
    except Exception as e:
        print("I did not get that, Can you please say again ? ")            
        speak("I did not get that, Can you please say again ? ")
        return "None"
    return query



if __name__=='__main__':
    
    WishMe()    
    while 1:
    
        query=takeCommand().lower() 
        if 'who are you' in query:
            
            print("\nHi lalit, I am alexa, you personal AI desktop assistant.I am specially built for telling weather,news, information from wikipedia,playing music,opening google as well as stack overflow. I can also tell time and i can open ms word as per your need")
            
            speak("Hi lalit, I am alexa, you personal AI desktop assistant, I am specially built for telling weather, news,  information from wikipedia, playing music, opening google as well as stack overflow, I can also tell time and i can open ms word as per your need")
            
            
        elif 'wikipedia' in query:
            
            res=wikipedia.summary(query,sentences=1)
            speak("\nAccording to wikipedia")
            print(res)
            speak(res)
            
            
        elif 'news' in query:
           
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from times of india, Happy reading")
            

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com/")
           
            
        elif 'open stack overflow' in query:
            webbrowser.open_new_tab("stackoverflow.com")
            

        elif 'music' in query:
            
            songs_dir= 'E:\\Music'
            songs=os.listdir(songs_dir)
            print(songs)
            os.startfile(os.path.join(songs_dir,random.choice(songs)))
            
            
        elif 'time' in query:
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak('the time is '+strTime)
            

        elif 'microsoft word' in query:
            
            wordpath='"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
            os.startfile(wordpath)
            print("I have opened ms word you can use now")
            speak("I have opened ms word you can use now")
            
        elif "weather" in query:
            
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
                
                print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))
                speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))

            else:
                speak(" City Not Found ")
            
            

        elif 'bye' in query:
            print("bye, thank you")
            speak('bye, thank you')
            break
            