import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import webbrowser

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')

def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said: ", text)
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not hear your request.")
            return None

def main():
    speak("Hello! How can I assist you today?")
    while True:
        command = get_audio()

        if command:
            if 'hello' in command:
                speak("Hello! How can I help you today?")

            elif 'time' in command:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {current_time}")

            elif 'date' in command:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")

            elif 'search' in command:
                speak("What do you want to search for?")
                query = get_audio()
                if query:
                    search_url = f"https://www.google.com/search?q={query}"
                    webbrowser.open(search_url)
                    speak(f"Here are the search results for {query}")

            elif 'exit' in command:
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I don't understand that command. Please try again.")

if __name__ == "__main__":
    main()
