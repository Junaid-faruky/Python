import time

input("Press Enter to start stopwatch")
start = time.time()
input("Press Enter to stop")
end = time.time()

print(f"Elapsed time: {end - start:.2f} seconds")
