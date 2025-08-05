import time
import os

sec = int(input("Seconds: "))
while sec:
    mins, secs = divmod(sec, 60)
    print(f"{mins:02}:{secs:02}", end="\r")
    time.sleep(1)
    sec -= 1
os.system('say "Time is up!"')  # Use 'say' for macOS, use other for Windows/Linux
