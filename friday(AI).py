import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import pyautogui

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    print(f"FRIDAY: {text}")
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        speak("Good morning sir, I am FRIDAY.")
    elif 12 <= hour < 18:
        speak("Good afternoon sir.")
    else:
        speak("Good evening sir.")
    speak("How can I assist you today?")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

def run_friday():
    greet()
    while True:
        command = listen()

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            result = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia:")
            speak(result)

        elif 'open youtube' in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")

        elif 'time' in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")

        elif 'date' in command:
            today = datetime.datetime.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif 'play' in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube.")
            pywhatkit.playonyt(song)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'screenshot' in command:
            image = pyautogui.screenshot()
            image.save("screenshot.png")
            speak("Screenshot taken and saved.")

        elif 'open notepad' in command:
            speak("Opening Notepad.")
            os.system("notepad")

        elif 'exit' in command or 'bye' in command or 'stop' in command:
            speak("Goodbye sir. FRIDAY signing off.")
            break

        elif command:
            speak("Searching that for you.")
            pywhatkit.search(command)

if __name__ == "__main__":
    run_friday()
