
import keyboard
from datetime import datetime


dicti = {}

def on_key_press(key):
    currentTime = datetime.now().strftime('%d/%m/%y %H:%M')
    if currentTime not in dicti:
        dicti[currentTime]=[]
    dicti[currentTime].append(key)
    print(dicti)

keyboard.on_press(on_key_press)
keyboard.wait('esc')



