import matplotlib.pyplot as plt
import random, time

data = [random.randint(1,100) for _ in range(20)]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                plt.bar(range(len(arr)), arr)
                plt.pause(0.1)
                plt.clf()

bubble_sort(data)
plt.show()
