import pywhatkit as kit
import requests
import socket

def search_on_google(query):
    kit.search(query)

def play_on_youtube(video):
    kit.playonyt(video)
    
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+34{number}", message)
    
def get_random_joke():
    response = {}
    response["error"] = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    try:
       s.connect(("www.google.com", 80))
    except (socket.gaierror, socket.timeout):
        response["error"] = "No tienes conexión a internet. Es necesario para que pueda realizar esta función."
    else:
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

def get_llum_off():
    response = {}
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get("https://www.buildyourexe.com/tuyapiphp-master/index.php?status=off", headers=headers)
    return response

def get_llum_on():
    response = {}
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get("https://www.buildyourexe.com/tuyapiphp-master/index.php?status=on", headers=headers)
    return response