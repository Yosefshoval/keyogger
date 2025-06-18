from time import strftime
from pynput import keyboard
from datetime import datetime


now = datetime.now()
y = now.strftime('%d/%m/%y %H:%M')
dicti = {}

def append_to_dict(char):
    global dicti,y
    try:
        dicti[y].append(char)
        print(dicti)
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift)
        dicti[y].append(char)
        print(dicti)


def on_key_press(key):
    global dicti,y
    key = str(key)[14]
    if y in dicti:
        if y == now:
            append_to_dict(key)
        else:
            dicti[now] = []
            append_to_dict(key)
    else:
        dicti[y] = []
        append_to_dict(key)


# Register the callback function

 # Waits until the 'esc' key is pressed to exit
keyboard.on_press(on_key_press)
keyboard.wait('esc')
print(dicti)
