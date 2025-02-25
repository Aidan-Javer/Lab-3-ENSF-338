import timeit

from matplotlib import pyplot as plt
import numpy as np

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def main():
    quicksort_time_arr = []
    list_lengths = [x for x in range(0, 505, 5)]
    for list_length in list_lengths:
        numbers = [x for x in range(list_length)]
        n = len(numbers)
        quicksort_time = timeit.timeit(lambda: quicksort(numbers, 0, n - 1), number=1)
        quicksort_time_arr.append(quicksort_time)
    
    plt.figure(figsize=(9, 7))
    plt.scatter(list_lengths, quicksort_time_arr, color='r', alpha=0.40, edgecolors="none", label="Quick Sort")
    coefficients = np.polyfit(list_lengths, quicksort_time_arr, 2)
    polynomial = np.poly1d(coefficients)
    plt.plot(list_lengths, polynomial(list_lengths), label="Interpolation Line", color='b')
    plt.title("Worst Case Complexity for Quick Sort")
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()

