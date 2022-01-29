from math import sqrt
arr = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,111,222]
x = 222

# find the value of x using jump search
def jumpsearch(arr, x):
    arrLen = len(arr)
    n = int(sqrt(arrLen))
    print("N: ", n)
    prev = 0

    for val in range(0, arrLen, n):
        if arr[val] == x:
            print("1: Found: @ ", val)
            return
        if arr[val] > x:
            for nVal in range(prev, val, 1):
                if arr[nVal] == x:
                    print("2: Found: @ ", nVal)
                    return
        if val + n >= arrLen:
            for nVal in range(val, arrLen, 1):
                if arr[nVal] == x:
                    print("3: Found: @ ", nVal)
                    return
        prev = val

jumpsearch(arr, x)
