import os
import subprocess as sp

paths = {
    'discord': "C:\\Users\\otino\\AppData\\Local\\Discord\\app-1.0.9149\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_calculator():
    sp.Popen(paths['calculator'])
    
def open_discord():
    os.startfile(paths['discord'])
