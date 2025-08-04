import time

seconds = int(input("Enter seconds to countdown: "))
while seconds:
    mins, secs = divmod(seconds, 60)
    print(f"{mins:02d}:{secs:02d}", end='\r')
    time.sleep(1)
    seconds -= 1
print("\nTime's up!")
