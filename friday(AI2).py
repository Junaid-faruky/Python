import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import pyjokes
import openai
import os

# OpenAI API (Optional - Replace with your key if using AI replies)
openai.api_key = 'YOUR_OPENAI_API_KEY'

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning! I am Friday.")
    elif 12 <= hour < 18:
        speak("Good Afternoon! I am Friday.")
    else:
        speak("Good Evening! I am Friday.")
    speak("How can I help you today?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("📖 Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"🗣️ User said: {command}\n")
    except Exception as e:
        print("🔇 Say that again please...")
        return "None"
    return command.lower()


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']


def run_friday():
    wish_me()
    while True:
        command = take_command()

        if 'wikipedia' in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            summary = wikipedia.summary(topic, sentences=2)
            speak("According to Wikipedia")
            speak(summary)

        elif 'play' in command:
            song = command.replace('play', '')
            speak(f"Playing {song} on YouTube...")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Current time is {time}")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'open notepad' in command:
            os.system("notepad")

        elif 'open chrome' in command:
            chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)

        elif 'send whatsapp' in command:
            speak("Who is the recipient?")
            # Phone number should be in format +91XXXXXXXXXX
            recipient = "+911234567890"
            speak("What is the message?")
            message = take_command()
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute + 2
            pywhatkit.sendwhatmsg(recipient, message, hour, minute)
            speak("Message scheduled successfully!")

        elif 'exit' in command or 'bye' in command:
            speak("Goodbye! Have a great day.")
            break

        elif 'chat' in command:
            speak("Ask me anything.")
            user_input = take_command()
            ai_reply = chat_with_gpt(user_input)
            speak(ai_reply)

        else:
            speak("I'm not sure how to help with that.")
