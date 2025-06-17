import keyboard
booli = True
while booli:
    event = keyboard.record(until='hhh555')
    print(event)
    if "hhh555" in event:
        break
# keyboard.play(event)

# print(list(keyboard.get_typed_strings(event)))


