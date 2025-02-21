import random
import timeit
from matplotlib import pyplot as plt

## Part 1 ##

def linear_search(arr, key):
    for index, value in enumerate(arr):
        if value == key:
            return index
    return -1

def partition_best(arr, low, high):   
    pivot = arr[(low + high) // 2]     
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

def binary_qsort_search(arr, key):
    lo = 0
    hi = len(arr) - 1
    quicksort_best(arr, lo, hi)
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


## Part 2 ##
def measure_time(search_func, array, key, iterations=100):
    t = timeit.timeit(lambda: search_func(array, key), number=iterations)
    return t / iterations

linear_avg = []
binary_qsort_avg = []

if __name__ in "__main__":
    average_linear = []
    average_binary_qsort = []
    listlengths = [x for x in range(0, 505, 5)]
    for listlength in listlengths:
        numbers = [x for x in range(listlength)]
        list1 = []
        list2 = []
        random_number = random.randint(numbers)
        for i in range(1000):
            list1.append(measure_time(linear_search, numbers, random_number))
        for j in range(1000):
            list2.append(measure_time(binary_qsort_search, numbers, random_number))
        avg_l = sum(list1) / len(list1)
        avg_b = sum(list2) / len(list2)
        average_linear.append(avg_l)
        average_binary_qsort.append(avg_b)


## Part 3 ##

## Part 4 ##
    slope, intercept = np.polyfit(listlengths, average_linear, 1)
    plt.scatter(listlengths, average_linear, label='Linear Search')
    linevalues = [slope * x + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'r')

    log_lengths = np.log(listlengths) 
    slope, intercept = np.polyfit(log_lengths, average_binary, 1)
    plt.scatter(listlengths, average_binary, label='Binary Search')
    linevalues = [slope * np.log(x) + intercept for x in listlengths]
    plt.plot(listlengths, linevalues, 'g')

    plt.xlabel('List Length')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()
"""
The linear search algorithm is significantly faster than the combination of qsort and binary search
because the average complexity of linear search is O(n) whereas the combination of qsort and binary sort is 
O(n(log(n))^2).
"""