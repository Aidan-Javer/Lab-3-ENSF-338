import ex6_avg as func
import random
import numpy as np
import matplotlib as plt

## Part 5 ##

if __name__ == "__main__":
    average_linear = []
    average_binary_qsort = []
    listlengths = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

    for listlength in listlengths:
        numbers = [x for x in range(listlength)]
        n = len(numbers)
        numbers_reverse = numbers[::-1]
        list1 = []
        list2 = []
        random_number = random.choice(numbers)
        list1.append(func.measure_time(func.linear_search, numbers_reverse, random_number))
        list2.append(func.measure_time(func.binary_qsort_search, numbers_reverse, random_number))
        avg_l = sum(list1) / len(list1)
        avg_b = sum(list2) / len(list2)
        average_linear.append(avg_l)
        average_binary_qsort.append(avg_b)
    slope, intercept = np.polyfit(listlengths, average_linear, 1)
    plt.scatter(listlengths, average_linear, label='Linear Search')
    plt.plot(listlengths, [slope * x + intercept for x in listlengths], 'r', label='Linear Fit')

    log_linear = listlengths * np.log(listlengths)  
    slope, intercept = np.polyfit(log_linear, average_binary_qsort, 1)
    plt.scatter(listlengths, average_binary_qsort, label='Quicksort/Binary Search')
    plt.plot(listlengths, slope * (listlengths * np.log(listlengths)) + intercept, 'g', label='Log Linear Fit')

    plt.xlabel('List Length')
    plt.ylabel('Average Time (seconds)')
    plt.legend()
    plt.show()

"""

"""