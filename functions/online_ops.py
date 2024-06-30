import pywhatkit as kit
import requests

def search_on_google(query):
    kit.search(query)

def play_on_youtube(video):
    kit.playonyt(video)
    
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+34{number}", message)
    
def get_random_joke():
    response = {}
    headers = {
           'Accept': 'application/json'
    }
    res = requests.get("https://v2.jokeapi.dev/joke/Any?lang=es", headers=headers).json()
    if res["type"] == "single":
        response["joke"] = res["joke"]
        response["answer"] = ""
    else:
        response["joke"] = res["setup"]
        response["answer"] = res["delivery"]
    return response