Import pyjoke
# pip install pyttsx3 import pyttsx3

# pip install speechRecognition import speech_recognition as sr #pip install Wikipedia
import wikipedia

import datetime
import webbrowser
import os
import smtplib
import subprocess
import winshell

# using inbuild voice from os engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[1].id) engine.setProperty('voice', voices[1].id)

# function for speak def speak(audio):
engine.say(audio)
engine.runAndWait()

# function for wish def wishMe():
hour = int(datetime.datetime.now().hour)

if hour >= 0 and hour < 12:
    speak("Good Morning!")

elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")

else:
    speak("Good Evening!")

speak(" Please tell me how may I help you")


# take command from user and return command into string

def takeCommand():


# It takes microphone input from the user and returns string output

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

try:
    print("Recognizing...")
query = r.recognize_google(audio, language='en-in')
print(f"User said: {query}\n")

except Exception as e:  #
print(e)
print("Say that again please...")
return "None"
return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if____name_____ == "____main____":
wishMe()
while True:
    # if 1:
    query = takeCommand().lower()

# Logic for executing tasks based on query if
'wikipedia' in query:
speak('Searching Wikipedia...')
query = query.replace("wikipedia", "")
results = wikipedia.summary(query, sentences=2)
speak("According to Wikipedia")
print(results)
speak(results)

elif 'open youtube' in query:
webbrowser.open("youtube.com")

elif 'open google' in query:
webbrowser.open("google.com")

elif 'open stackoverflow' in query:
webbrowser.open("stackoverflow.com")

elif 'play music' in query:
music_dir = 'D:\\Non Critical\\songs'
songs = os.listdir(music_dir)
print(songs)
os.startfile(os.path.join(music_dir, songs[0]))

elif 'the time' in query:
strTime = datetime.datetime.now().strftime("%H:%M:%S")
speak(f"Sir, the time is {strTime}")

elif 'open code' in query:

codePath
"C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
os.startfile(codePath)

elif 'email to satish' in query:
try:
    speak("What should I say?")
content = takeCommand()
to = "satishyourEmail@gmail.com"
sendEmail(to, content)
speak("Email has been sent!")
except Exception as e:
print(e)
speak("Sorry my friend . I am not able to send this email")

elif "write a note" in query:
speak("What should i write, sir")
note = takeCommand()
file = open('jarvis.txt', 'w')
speak("Sir, Should i include date and time")

snfm = takeCommand()
if 'yes' in snfm or 'sure' in snfm:
    strTime = datetime.datetime.now().strftime("% H:% M:% S")
    file.write(strTime)
file.write(" :- ")
file.write(note)
else:
file.write(note)
# complete the task


elif "show note" in query: speak("Showing Notes")
file = open("jarvis.txt", "r")
print(file.read())
speak(file.read(6))

elif "where is" in query:
query = query.replace("where is", "")
location = query
speak("User asked to Locate")
speak(location)

webbrowser.open("https://www.google.nl / maps / place/" + location + "")

elif "don't listen" in query or "stop listening" in query:
speak("for how much time you want to stop jarvis from listening commands")
a = int(takeCommand())
time.sleep(a)
print(a)

elif 'shutdown system' in query:
speak("Hold On a Sec ! Your system is on its way to shutdown")
subprocess.call('shutdown / p /f')

elif "restart" in query:
subprocess.call(["shutdown", "/r"])

elif "hibernate" in query or "sleep" in query: speak("Hibernating")
subprocess.call("shutdown / h")

elif "log off" in query or "sign out" in query:

speak("Make sure all the application are closed before sign-out")
time.sleep(5)
subprocess.call(["shutdown", "/l"])

elif 'how are you' in query:
speak("I am fine, Thank you")
speak("How are you, Sir")

elif 'fine' in query or "good" in query:
speak("It's good to know that your fine")

elif "change my name to" in query:
query = query.replace("change my name to", "")
name = query

elif "change name" in query:
speak("What would you like to call me, Sir ")
name = takeCommand()
speak("Thanks for naming me")

elif "what's your name" in query or "What is your name" in query: speak("My friends call me")
speak(name)

print("My friends call me", name)

elif 'exit' in query:
speak("Thanks for giving me your time")
exit()

elif "who made you" in query or "who created you" in query: speak("I have been created by abhinav.")

elif 'joke' in query: speak(pyjokes.get_joke())

elif 'search' in query or 'play' in query: query = query.replace("search", "")
query = query.replace("play", "")
webbrowser.open(query)

elif "who i am" in query:
speak("you are abhinav.")

elif "why you came to world" in query: speak("Thanks to abhinav. further It's a secret")

elif 'power point presentation' in query:
speak("opening Power Point presentation")
power = r"C:\\Users\\Desktop\\Minor
Project\\Presentation\\Voice
Assistant.pptx
" os.startfile(power)

elif "who are you" in query:
speak("I am your virtual assistant ")

elif 'reason for you' in query:
speak("I was created as a Minor project”)

elif 'empty recycle bin' in query:
winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
speak("Recycle Bin Recycled")

elif 'good bye' in query: speak("have a nice day")
exit()