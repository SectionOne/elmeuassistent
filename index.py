import speech_recognition as sr
import json
import pyttsx3

engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 120)

# Set Languatge
engine.setProperty('voice', 'spanish')

# Set Volume
engine.setProperty('volume', 1.0)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as src:
        rec.adjust_for_ambient_noise(src)
        audio = rec.listen(src)
    try:
        cmd = rec.recognize_vosk(audio)
    except Exception:
        print("No puc entendre't. Intenta escriure-ho?")
        cmd = input()
    return cmd

def listenToText():
    c = listen()
    #print("Valor escoltat=",c)
    d = json.loads(c)
    return str(d["text"])

speak("Hola buenos dias. En que te puedo ayudar?")
print(listenToText())
print("Hola Classe que tal?")