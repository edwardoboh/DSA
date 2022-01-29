import random
# Implementation of Buble Sort Algorithm in Python
arr = [15, 1, 13, 5, 18, 2, 8, 3, 6, 12, 4, 19, 7, 9, 16, 14, 10, 0, 11, 17]

def bubble(arr):
    n = len(arr)
    for _ in range(n-1):
        for elem in range(n-1):
            if arr[elem] > arr[elem + 1]:
                arr[elem], arr[elem+1] = arr[elem+1], arr[elem]
    print("Sorted Array: ", arr)

b = range(10000)
b = list(b)
random.shuffle(b)
# print("B: ", b)
bubble(b)
