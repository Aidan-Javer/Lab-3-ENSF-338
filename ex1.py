def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    n1 = mid - low + 1              # First, calculate the length of the subarray on the left
    n2 = high - mid                 # and the subarray on the right

    T1 = [0] * n1                   # Create two temporary arrays, T1 and T2, each of which will
    T2 = [0] * n2                   # be a slong as their corresponding sub-array

    for i in range(0, n1):          # Now, iterate through a for loop. For each element in range (0, n1)
        T1[i] = arr[low + i]        # add the elements of the subarray on the left to T1
    for j in range(0, n2):          # for each element in range (0, n2)
        T2[j] = arr[mid + 1 + j]    # add the elements of the subarray on the right to T2
    
    i = 0                           # Initialize i to the start of T1
    j = 0                           # Initialize j to the start of T2
    k = low                         # Initialize k to the start of the original array

    while i < n1 and j < n2:        # While i [0] is less than n1 [length of T1] and j [0] is less than n2 [length of T2]
        if T1[i] <= T2[j]:          # compare the elements of T1 and T2. If T1[i] is less than or equal to T2[j]
            arr[k] = T1[i]          # add T1[i] to the original array and
            i += 1                  # increment i.
        else:                       # Otherwise, if T1[i] is greater than T2[j]  
            arr[k] = T2[j]          # add T2[j] to the original array and
            j += 1                  # increment j.
        k += 1                      # lastly, increment k. 
        
    # if there are left over values (caused by difference in size for T1 and T2),
    # iterate through a while loop, adding any leftover values from T1 and T2 to the original array
    # and incrementing i, j, and k accordingly.
    
    while i < n1:
        arr[k] = T1[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = T2[j]
        j += 1
        k += 1
