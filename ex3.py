import random
from matplotlib import pyplot as plt
import numpy as np


## Part a ##
"""
Number of Comparison:
- The largest element bubbles to the top on every pass:
    First pass: n-1 comparisons
    Second pass: n-2 comparisons
    ... Final pass: 1 comparison
- Group together we get: (n-1) + (n-2) ... + 1 = n * (n-1)/2 = O(n^2)

Number of Swaps:
- Swaps occur when passing through and comparing each element. When comparing two random elements 
the probability of them being swapped is 1/2. Therefore, the total number of comparisons * the
probability of being swapped is n * (n-1) / 2 * 1 / 2 = n * (n-1) / 4 = O(n^2)
"""

## Part b ##
def bubble_sort(arr):
    num_swaps = 0
    num_comps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            num_comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                num_swaps += 1
    return num_comps, num_swaps

## Part c ##
list_lengths = [x for x in range(100, 1000, 50)]
number_of_comparisons = []
number_of_swaps = []

if __name__ == "__main__":
    for list_length in list_lengths:
        numbers = [x for x in range(list_length)]
        n = len(numbers)
        numbers_shuffle = random.sample(numbers, n)
        num_comps, num_swaps = bubble_sort(numbers_shuffle)
        number_of_comparisons.append(num_comps)
        number_of_swaps.append(num_swaps)

## Part d ##
    x = np.array(list_lengths)
    
    comparisons_coefficent = np.polyfit(x, number_of_comparisons, 2)
    comparisons_equation = np.poly1d(comparisons_coefficent)
    comparisons_line = comparisons_equation(x)
    
    plt.scatter(x, number_of_comparisons, label='#Comparisons', color='red')
    plt.plot(x, comparisons_line, 'r--', label='Quadratic Fit Comparisons')
    
    swap_coefficient = np.polyfit(x, number_of_swaps, 2)
    swaps_equation = np.poly1d(swap_coefficient)
    swaps_line = swaps_equation(x)
    
    plt.scatter(x, number_of_swaps, label='#Swaps', color='blue')
    plt.plot(x, swaps_line, 'b-.', label='Quadratic Fit Swaps')
    
    plt.xlabel('List Length')
    plt.ylabel('Count')
    plt.title('Bubble Sort Comparisons and Swaps vs. List Length')
    plt.legend()
    plt.show()

"""
The data does fit the complexity analysis discussed in part a as both the number of swaps and the number of comparisons
have quadratic complexity n^2 where the number of comparisons is roughly double the number of swaps which is shown in the
plots.
"""

