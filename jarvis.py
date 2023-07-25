import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
        
    elif hour>=12 and hour<18:
        speak("Good afternoon")
        
    else:
        speak("Good evening")
        
    speak('First of all thanku sir to intract with me')
    speak('I hope you are doing great sir')
    speak('So my name is jarvis sir,please tell me how i help you')

    
def takeCommand():
    # it takes microophone input from user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('harshk2807@gmail.com','xnxzmmcbzwsoncpg')
    server.sendmail('harshk2807@gmail.com',to,content)
    server.close()

if __name__ ==  "__main__":
    wishMe()

# while True:   
if 1:
    # takeCommand()
    query=takeCommand().lower()
     
    # logic for executing tasks
    if 'wikipedia' in query:
        speak('Searching wikipedia..')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
        
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    
    elif 'open google' in query:
        webbrowser.open("google.com")
    
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
        
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
        
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
        
    # elif 'play music' in query:
        # music_dir='C:\Users\91978\Desktop\Newfolder\Musicapp'
        # songs=os.listdir(music_dir)
        # print(songs)
        # os.startfile(os.path.join(music_dir),songs[0])
        
    elif 'the time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
        
    elif 'open code' in query:
        codePath="C:\\Users\\91978\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        
    elif 'email to harsh' in query:
        try:
            speak("What should I say?")
            content=takeCommand()
            to="harshk2807@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
            
        except Exception as e:
            print(e)
            speak("Sorry my friend harsh bhai. I am not able to send this email")
        
        