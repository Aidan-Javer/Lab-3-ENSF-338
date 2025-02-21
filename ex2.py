import random
import timeit
from matplotlib import pyplot as plt
#import numpy as np

import sys
sys.setrecursionlimit(2000)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def partition(arr, low, high):      #Chooses first element of array as pivot
    pivot = arr[low]
    left = low + 1
    right = high
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index+1, high)

def partition_best(arr, low, high):     #Chooses middle element of array as pivot
    pivot = arr[(low + high) // 2]      #Floor division to ensure result is an integer
    left = low + 1
    right = high
    done = False

    arr[low], arr[(low + high) // 2] = arr[(low + high) // 2], arr[low]

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def quicksort_best(arr, low, high):
    if low < high:
        pivot_index = partition_best(arr, low, high)
        quicksort_best(arr, low, pivot_index)
        quicksort_best(arr, pivot_index+1, high)

list_lengths = [x for x in range(0, 105, 5)]
bubble_best_avg = []
bubble_avg_avg = []
bubble_worst_avg =[]

quicksort_best_avg = []
quicksort_avg_avg = []
quicksort_worst_avg =[]

for list_length in list_lengths:
    numbers = [x for x in range(list_length)]
    n = len(numbers)

    bubble_best_times = []
    bubble_avg_times = []
    bubble_worst_times = []

    quicksort_best_times = []
    quicksort_avg_times = []
    quicksort_worst_times = []

    for i in range(100):
        numbers_reverse = numbers[::-1]
        numbers_shuffle = random.sample(numbers, n)

        numbers_copy = numbers[:]
        numbers_reverse_copy = numbers_reverse[:]
        numbers_shuffle_copy = numbers_shuffle[:]

        #Best case for bubble sort: Array is already sorted
        #Best case for quick sort: Array is partitionined in half every time
        bubble_best_tm = timeit.timeit(lambda: bubble_sort(numbers), number=1)
        bubble_best_times.append(bubble_best_tm)
        quicksort_best_tm = timeit.timeit(lambda: quicksort_best(numbers_copy, 0, n-1), number=1)
        quicksort_best_times.append(quicksort_best_tm)

        bubble_avg_tm = timeit.timeit(lambda: bubble_sort(numbers_shuffle), number=1)
        bubble_avg_times.append(bubble_avg_tm)
        quicksort_avg_tm = timeit.timeit(lambda: quicksort(numbers_shuffle_copy, 0, n-1), number=1)
        quicksort_avg_times.append(quicksort_avg_tm)

        #Worst case for bubble sort: Array is sorted in reverse
        #Worst case for quick sort: Each partition results in a subarray of size 1
        bubble_worst_tm = timeit.timeit(lambda: bubble_sort(numbers_reverse), number=1)
        bubble_worst_times.append(bubble_worst_tm)
        quicksort_worst_tm = timeit.timeit(lambda: quicksort(numbers_reverse_copy, 0, n-1), number=1)
        quicksort_worst_times.append(quicksort_worst_tm)
    
    bubble_best_avg_tm = sum(bubble_best_times) / len(bubble_best_times)
    bubble_best_avg.append(bubble_best_avg_tm)
    bubble_avg_avg_tm = sum(bubble_avg_times) / len(bubble_avg_times)
    bubble_avg_avg.append(bubble_avg_avg_tm)
    bubble_worst_avg_tm = sum(bubble_worst_times) / len(bubble_worst_times)
    bubble_worst_avg.append(bubble_worst_avg_tm)

    quicksort_best_avg_tm = sum(quicksort_best_times) / len(quicksort_best_times)
    quicksort_best_avg.append(quicksort_best_avg_tm)
    quicksort_avg_avg_tm = sum(quicksort_avg_times) / len(quicksort_avg_times)
    quicksort_avg_avg.append(quicksort_avg_avg_tm)
    quicksort_worst_avg_tm = sum(quicksort_worst_times) / len(quicksort_worst_times)
    quicksort_worst_avg.append(quicksort_worst_avg_tm)

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), bubble_best_avg, color='r', label="Bubble Sort")
plt.scatter(range(0, 105, 5), quicksort_best_avg, color='b', label="Quick Sort")
plt.title("Best Case Scenarios for Bubble and Quick Sort")
plt.legend()
plt.savefig("ex2_best.png")

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), bubble_avg_avg, color='r', label="Bubble Sort")
plt.scatter(range(0, 105, 5), quicksort_avg_avg, color='b', label="Quick Sort")
plt.title("Average Case Scenarios for Bubble and Quick Sort")
plt.legend()
plt.savefig("ex2_avg.png")

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), bubble_worst_avg, color='r', label="Bubble Sort")
plt.scatter(range(0, 105, 5), quicksort_worst_avg, color='b', label="Quick Sort")
plt.title("Worst Case Scenarios for Bubble and Quick Sort")
plt.legend()
plt.savefig("ex2_worst.png")
