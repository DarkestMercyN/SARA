import pyttsx3    #to convert text to speech
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser #to search something on browser
import os       #to open something within our system
import smtplib  #for mailing purpose

engine = pyttsx3.init('sapi5')         #sapi5 is Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft.
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")    

    speak("How may I help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")   

    except Exception as e:
        #print(e)

        print("Say that again please...")    
        return "None"
    return query


# To send Email
#def sendEmail(to, content):
   # server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('email_id', 'pswrd') 
    #server.sendEmail('email_id', to, content)
    #server.close()

if __name__ == "__main__": 
    wishMe()
    while True:   #for continuously running th ai. For only once, use 'if 1:'
        query = takeCommand().lower()

       #logic for executing tasks
        if 'wikipedia' in query:
           speak("Searching Wikipedia....")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=2)
           speak("According to wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
           webbrowser.open("youtube.com") 

        elif 'open google' in query:
           webbrowser.open("google.com")       

        elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")   

        elif 'open spotify' in query:
           webbrowser.open("spotify.com") 

        elif 'open chess' in query:
           webbrowser.open("chess.com")
        
        elif 'play video' in query:
            vidPath = "C:\\Users\\DELL\\Pictures\\Saved Pictures\\Video.mp4"
            os.startfile(vidPath)    

#if music already in computer
        #elif 'play music' in query:
           #music_dir = address of songs
           # songs = os.listdir(music_dir)
           # print(songs)         

        elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S") 
           speak(f"The time is {strTime}") 
        
        elif 'the date' in query:
            strDate = datetime.datetime.today().strftime("%d:%B:%Y")
            speak(f"The date is {strDate}")  
        
        elif 'who are you' in query:
            speak("I am Sara. I am a virtual assistant. Ask me anything and i will try to complete the task for you.")
            print("I am Sara. I am a virtual assistant. Ask me anything and i will try to complete the task for you.")

        elif 'open code' in query:
            codePath = "C:\\Users\\nishant\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Code.exe" 
            os.startfile(codePath)  
        
        elif 'open website' in query:
            webPath = "C:\\Users\\DELL\\Documents\\Website\\Front.html"
            os.startfile(webPath)

        # elif 'email to Aditya' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "email_id"
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry sir i am not able to send email!")    
