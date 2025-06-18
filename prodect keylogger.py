
import keyboard
from datetime import datetime


dicti = {}
dicti_for_show = {"all times":''}

def on_key_press(key):
    global dicti_for_show
    key = str(key)[14:-6]
    currentTime = datetime.now().strftime('%d/%m/%y %H:%M')

    if currentTime not in dicti:
        dicti[currentTime] = ''

    dicti[currentTime] += key
    dicti_for_show["all times"] += key
    print(key)

    if "show" in dicti_for_show["all times"]:
        for k,v in dicti_for_show.items():
            print(k)
            print(v)
        dicti_for_show = {}


keyboard.on_press(on_key_press)
keyboard.wait('Ctrl + Shift + .')

for k, v in dicti.items():
    print(k)
    print(v)
    print()