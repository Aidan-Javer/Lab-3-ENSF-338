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
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        elif arr[mid] > val:
            end = mid - 1
        else:
            return mid
    return start

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        for k in range(i, j, -1):
            arr[k] = arr[k - 1]
        arr[j] = val
    return arr

list_lengths = [x for x in range(0, 1050, 50)]
insertion_avg = []
binary_insertion_avg = []

for list_length in list_lengths:
    numbers = [x for x in range(list_length)]
    insertion_times = []
    binary_insertion_times = []

    for i in range(100):
        random.shuffle(numbers)
        numbers_copy = numbers[:]

        insertion_tm = timeit.timeit(lambda: insertion_sort(numbers), number=1)
        insertion_times.append(insertion_tm)
        binary_insertion_tm = timeit.timeit(lambda: binary_insertion_sort(numbers_copy), number=1)
        binary_insertion_times.append(binary_insertion_tm)

    insertion_avg_tm = sum(insertion_times) / len(insertion_times)
    insertion_avg.append(insertion_avg_tm)
    binary_avg_tm = sum(binary_insertion_times) / len(binary_insertion_times)
    binary_insertion_avg.append(binary_avg_tm)

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 1050, 50), insertion_avg, color='r', label="Insertion Sort")
plt.scatter(range(0, 1050, 50), binary_insertion_avg, color='b', label="Binary Insertion Sort")
plt.title("Average Case Scenarios for Insertion and Binary Insertion Sort")
plt.legend()
plt.savefig("ex5.png")

"""
Question 4:
Binary insertion sort is faster than traditional insertion sort. This is because traditional insertion sort uses linear search to find the insertion position for each element, wherease binary insertion sort uses binary search to find the insertion position for each element. The binary search reduces the complexity of the number of comparisons from O(N) to O(logN). Binary search can be applied since the search occurs in the sorted subarray so it is possible to use the divide and conquer methodology of binary search. While binary insertion sort is faster than traditional insertion sort, it is important to note that they both have an average case complexity of O(n^2). Binary insertion sort can be considered as an optimization of tradition insertion sort.
"""