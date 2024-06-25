import speech_recognition as sr
import json

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
    print("Valor escoltat=",c)
    d = json.loads(c)
    return str(d["text"])

print(listenToText())
print("Hola Classe que tal?")