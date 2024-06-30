import pywhatkit as kit

def search_on_google(query):
    kit.search(query)

def play_on_youtube(video):
    kit.playonyt(video)
    
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+34{number}", message)