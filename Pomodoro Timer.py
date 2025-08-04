import time

work = 25 * 60  # seconds
break_time = 5 * 60

def countdown(sec, label):
    while sec:
        mins, secs = divmod(sec, 60)
        print(f"{label} - {mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        sec -= 1
    print(f"{label} done!              ")

countdown(work, "Work")
countdown(break_time, "Break")
