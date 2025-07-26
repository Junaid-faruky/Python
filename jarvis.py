import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import pyautogui

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Speed
engine.setProperty('volume', 1.0)  # Volume

def speak(text):
    print(f"🗣️ JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, sir!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir!")
    else:
        speak("Good Evening, sir!")
    speak("I am Jarvis. How can I assist you today?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        print(f"👤 You: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is unavailable.")
        return ""

def main():
    greet_user()
    while True:
        command = take_command()

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia:")
            speak(results)

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif 'play' in command:
            song = command.replace("play", "")
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'screenshot' in command:
            speak("Taking screenshot")
            image = pyautogui.screenshot()
            image.save("screenshot.png")
            speak("Screenshot saved")

        elif 'exit' in command or 'bye' in command:
            speak("Goodbye, sir!")
            break

        elif command:
            speak("I can search that for you.")
            pywhatkit.search(command)

if __name__ == "__main__":
    main()
