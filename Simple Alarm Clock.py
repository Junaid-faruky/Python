import datetime
import time
import os

alarm_time = input("Set alarm (HH:MM:SS): ")

while True:
    now = datetime.datetime.now().strftime("%H:%M:%S")
    if now == alarm_time:
        print("Wake up!")
        # Windows only
        os.system("start alarm.mp3")
        break
    time.sleep(1)
