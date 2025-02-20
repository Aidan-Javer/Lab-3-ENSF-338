import random
import timeit
from matplotlib import pyplot as plt
import numpy as np

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
    pivot = arr[(low  + high) // 2]      #Floor division to ensure result is an integer
    left = low + 1
    right = high
    done = False

    arr[low], arr[(low  + high) // 2] = arr[(low  + high) // 2], arr[low]

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
bubble_best_times = []
bubble_avg_times = []
bubble_worst_times = []

quicksort_best_times = []
quicksort_avg_times = []
quicksort_worst_times = []


for list_length in list_lengths:
    numbers = [x for x in range(list_length)]
    n = len(numbers)

    numbers_reverse = numbers[::-1]
    numbers_shuffle = random.sample(numbers, n)
    random.shuffle(numbers_shuffle)

    #Best case for bubble sort: Array is already sorted
    #Best case for quick sort: Array is partitionined in half every time
    bubble_best_tm = timeit.timeit(lambda: bubble_sort(numbers), number=100)
    bubble_best_times.append(bubble_best_tm / 10)
    quicksort_best_tm = timeit.timeit(lambda: quicksort_best(numbers, 0, n-1), number=100)
    quicksort_best_times.append(quicksort_best_tm / 10)

    bubble_avg_tm = timeit.timeit(lambda: bubble_sort(numbers_shuffle), number=100)
    bubble_avg_times.append(bubble_avg_tm / 10)
    quicksort_avg_tm = timeit.timeit(lambda: quicksort(numbers_shuffle, 0, n-1), number=100)
    quicksort_avg_times.append(quicksort_avg_tm / 10)

    #Worst case for bubble sort: Array is sorted in reverse
    #Worst case for quick sort: Each partition results in a subarray of size 1
    bubble_worst_tm = timeit.timeit(lambda: bubble_sort(numbers_reverse), number=100)
    bubble_worst_times.append(bubble_worst_tm / 10)
    quicksort_worst_tm = timeit.timeit(lambda: quicksort(numbers_reverse, 0, n-1), number=100)
    quicksort_worst_times.append(quicksort_worst_tm / 10)

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), bubble_best_times, color='r')
plt.scatter(range(0, 105, 5), quicksort_best_times, color='b')
plt.title("Best Case Scenarios for Bubble and Quick Sort")
plt.savefig("ex2_best.png")

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), bubble_avg_times, color='r')
plt.scatter(range(0, 105, 5), quicksort_avg_times, color='b')
plt.title("Average Case Scenarios for Bubble and Quick Sort")
plt.savefig("ex2_avg.png")

plt.figure(figsize=(9, 7))
plt.scatter(range(0, 105, 5), bubble_worst_times, color='r')
plt.scatter(range(0, 105, 5), quicksort_worst_times, color='b')
plt.title("Worst Case Scenarios for Bubble and Quick Sort")
plt.savefig("ex2_worst.png")
