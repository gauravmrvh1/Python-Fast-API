import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print("ID:", voice.id)
    print("Name:", voice.name)
    print("Gender:", voice.gender if hasattr(voice, 'gender') else "Unknown")
    print("-" * 30)



# engine.setProperty('voice', voices[0].id)  # Male usually 0
# engine.say("Hello Gaurav, this is male voice")
# engine.runAndWait()

engine.setProperty('voice', voices[1].id)  # Female usually 1
engine.say("Hello Pooja, this is female voice")
engine.runAndWait()