import speech_recognition as sr
import json
import pyttsx3
from datetime import datetime

USERNAME = "Usuario"
BOTNAME = "laura"
inactivity = 0
greet = False
dialog = False

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

def greet_user():
    """Greets the user according to the time"""
    global greet
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Buenos dias {USERNAME}")
    elif (hour >= 12) and (hour < 19):
        speak(f"Buenas tardes {USERNAME}")
    elif (hour >= 19) or (hour <= 23):
        speak(f"Buenas noches {USERNAME}")
    speak(f"Mi nombre es {BOTNAME}. Como puedo ayudarte?")
    greet = True

def byeBye():
    global greet,dialog
    hour = datetime.now().hour
    if hour >= 21 or hour < 6:
        speak("Buenas noches, cuidate mucho!")
    else:
        speak('Que tengas un buen dia!')
        print(hour)
    dialog = False
    greet = False

def listenToText():
    c = listen()
    #print("Valor escoltat=",c)
    d = json.loads(c)
    return str(d["text"])

#Funció per observar si un string es troba a una llista
def isContain(textInput,seeds):
    response = False
    for seed in seeds:
        if textInput.find(seed) > -1: 
            response = True 
    return response

#Sequencia d'entrada en conversació
def inDialog():
    global dialog
    stringInput = listenToText()
    if isContain(stringInput,["hola " + BOTNAME,"ajudem " + BOTNAME,BOTNAME]):
        dialog = True
        
while True:
    #Control de si s'ha iniciat conversació o no
    if dialog:
        #Validació de la salutació
        if inactivity == 0 and greet == False : greet_user()
        stringInput = listenToText()
        
        if isContain(stringInput,['adiós', 'adeu', 'ves a dormir', 'finaliza', 'finalitza', 'quit', 'terminate', 'kill', 'end']):
            byeBye()
            continue #Situarem continue per tornar a la següent repetició del cicle
              
        print("Fi del cicle")
    else:
        print("In StandBy")
        inDialog()