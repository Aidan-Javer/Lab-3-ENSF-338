import random
import timeit
import matplotlib.pyplot as plt
import json

def binary_search(arr, target, low, high, initial_midpoint=None):
    if low > high:
        return -1  # Target not found

    if initial_midpoint is not None:
        mid = initial_midpoint
        initial_midpoint = None  # Reset after the first iteration
    else:
        mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high, initial_midpoint)
    else:
        return binary_search(arr, target, low, mid - 1, initial_midpoint)

# Example usage
if __name__ == "__main__":
    mid_arr = []
    infile = open("ex7data.json", "r")
    arr = json.load(infile)
    infile = open("ex7tasks.json", "r")
    targets = json.load(infile)
    for target in targets:
        data_dict = {}
        for i in range(0, 500):
            in_mid = random.randint(0, len(arr) - 1)
            elapsed_time = timeit.timeit(lambda: binary_search(arr, target, 0, len(arr) - 1, in_mid), number=1)
            data_dict[elapsed_time] = in_mid
        best_time = min(data_dict.keys())
        mid_arr.append(data_dict[best_time])

    
    plt.figure(figsize=(9, 7))
    plt.scatter(mid_arr, targets, color='r', alpha=0.40, edgecolors="none", label="Midpoint Analysis")
    plt.title("mid_arr vs. targets")
    plt.xlabel("mid_arr")
    plt.ylabel("targets")
    plt.show()
    
# QUESTION 4
"""
Looking at the graph, there seems to be a linear trend, implying that 
if the midpoint is closer to the target, the time it takes to find the target is reduced.
This is because the closer the midpoint is to the target, the fewer comparisons are needed 
to find the target.
"""