import psutil
import time

while True:
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | RAM: {mem}%")
    time.sleep(2)
