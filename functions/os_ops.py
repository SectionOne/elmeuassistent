import os
import subprocess as sp

paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def open_calculator():
    sp.Popen(paths['calculator'])
