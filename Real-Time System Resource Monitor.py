import psutil, time

while True:
    print(f"CPU: {psutil.cpu_percent()}% | RAM: {psutil.virtual_memory().percent}%")
    time.sleep(1)
