# import keyboard
# booli = True
# while booli:
#     event = keyboard.record(until='hhh555')
#     print(event)
#     if "hhh555" in event:
#         break
# # keyboard.play(event)

# print(list(keyboard.get_typed_strings(event)))





from pynput import keyboard
from datetime import datetime

# def on_press(key):
#     try:
#         print('alphanumeric key {0} pressed'.format(
#             key.char))
#     except AttributeError:
#         print('special key {0} pressed'.format(
#             key))
#
# times = {}
#
# while True:
#     listiner = on_press(keyboard.Listener)
#     if datetime.now() in times:
#         times[datetime.now()] += Listener
#     else:
#         times[datetime.now()] = listiner
#
#
# print(times)


import keyboard

# y = now.strftime('%d/%m/%y %H:%M')

dicti = {}

def on_key_press(key):
    now = datetime.now().strftime('%d/%m/%y %H:%M')
    global dicti,y
    if datetime.minute in dicti:
        if datetime.now() == now:
            try:
                dicti[datetime.now()].append(key)
                print(dicti)
            except AttributeError:
                # Handle special keys (e.g., space, enter, shift)
                dicti[datetime.now()].append(key)
                print(dicti)
        else:
            dicti[datetime.now()] = []
            try:
                dicti[datetime.now()].append(key)
                print(dicti)
            except AttributeError:
                # Handle special keys (e.g., space, enter, shift)
                dicti[datetime.now()].append(key)
                print(dicti)
    else:
        dicti[datetime.now()] = []
        try:
            dicti[datetime.now()].append(key)
            print(dicti)
        except AttributeError:
            # Handle special keys (e.g., space, enter, shift)
            dicti[datetime.now()].append(key)
            print(dicti)

# Register the callback function
# while True:
#     if  y == x:
#         keyboard.wait('esc')
#     else:
#         dicti[y] = []
#         keyboard.on_press(on_key_press)
#         keyboard.wait('esc')
# Keep the program running to listen for events
 # Waits until the 'esc' key is pressed to exit
keyboard.on_press(on_key_press)
keyboard.wait('esc')
print(dicti)
