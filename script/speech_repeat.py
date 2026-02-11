import speech_recognition as sr
import pyttsx3

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("🎤 Kuch bolo...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 Tumne bola:", text)

    # Repeat the same text
    engine.say(text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Samajh nahi aaya 😅")

except sr.RequestError:
    print("Internet issue")
