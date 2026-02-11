import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("🎤 Bolna shuru karo...")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("📝 Text:", text)

except sr.UnknownValueError:
    print("Samajh nahi aaya 😅")

except sr.RequestError:
    print("Internet issue")
