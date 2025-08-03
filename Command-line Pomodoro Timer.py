import time

work = 25 * 60
break_time = 5 * 60

def countdown(seconds, label):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{label} - {mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    print(f"{label} done!         ")

countdown(work, "Work")
countdown(break_time, "Break")
