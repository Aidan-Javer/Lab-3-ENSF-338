import random
import timeit
from matplotlib import pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
    
    if start > end:
        return start
    
    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

list_lengths = [x for x in range(0, 105, 5)]
insertion_times = []
binary_insertion_times = []

for list_length in list_lengths:
    numbers = [x for x in range(list_length)]
    #n = len(numbers)

    random.shuffle(numbers)

    insertion_tm = timeit.timeit(lambda: insertion_sort(numbers), number=100)
    insertion_times.append(insertion_tm / 100)
    binary_insertion_tm = timeit.timeit(lambda: binary_insertion_sort(numbers), number=100)
    binary_insertion_times.append(binary_insertion_tm / 100)

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), insertion_times, color='r', label="Insertion Sort")
plt.scatter(range(0, 105, 5), binary_insertion_times, color='b', label="Binary Insertion Sort")
plt.title("Average Case Scenarios for Insertion and Binary Insertion Sort")
plt.legend()
plt.savefig("ex5.png")
