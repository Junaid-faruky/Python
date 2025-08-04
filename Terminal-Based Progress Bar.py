import time
def progress(total):
    for i in range(total+1):
        percent = i / total * 100
        bar = '#' * (i*30//total) + '-' * (30 - i*30//total)
        print(f"[{bar}] {percent:5.1f}%", end='\r')
        time.sleep(0.1)
    print("\nDone.")

progress(100)
