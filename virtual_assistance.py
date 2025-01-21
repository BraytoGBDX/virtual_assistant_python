import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

#initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """MAke the assistant speaks"""
    engine.say(text)
    engine.runAndWait()
    
def listen():
    """Listens to the microphone and converts speech to text"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="en-US,es-ES")
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry i dont understand")
            return ""
        except sr.RequestError:
            print("Server error")
            return ""
        
def tell_time():
    """Tells the current time"""
    current_time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {current_time}")
    
def search_web(query):
    """Performs a web search"""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here is what a found for: {query}")
    
def main():
    """Main loop for assistant"""
    speak("Hello, i am Gray your virtual assistance. How can i help you today?")
    while True:
        command = listen()
        
        if "exit" in command or "salir" in command:
            speak("see you next time")
            break
        elif "time" in command or "hora" in command:
            tell_time()
        elif "search" in command or "busca" in command:
            speak("What would you like search for?")
            query = listen()
            if query:
                search_web()
            else:
                speak("i dont understand that")
        elif "hello" in command or "hola" in command:
            speak("Hi darling, how are you today?")
        elif "your name" in command or "tu nombre" in command:
            speak("My name is gray and i am your virtual assistant")
        else:
            speak("i´m not sure how to respond to that.")
    