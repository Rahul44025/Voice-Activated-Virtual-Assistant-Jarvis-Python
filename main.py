import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests

#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "8357a6be3f75421ba9cd37dc64d84e98"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open amazon" in c.lower():
        webbrowser.open("https://amazon.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the json response
            data = r.json()
            #Extract the articles
            articles = data.get("articles", [])
            #Print the headlines
            for article in articles:
                speak(article["title"])
    else:
        #Let OpenAI hanle the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #Listen fot the wake word "Jarvis"
        # obtain audio from the microphone

        r = sr.Recognizer()
        
        print("recognizing...")

        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...  ")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio) 
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...  ")
                    audio = r.listen(source)
                    command = r.recognize_google(audio) 

                    processCommand(command)
        
        except Exception as e:
            print("Error {0}".format(e))