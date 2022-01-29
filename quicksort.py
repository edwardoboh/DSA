import random
# Bsically similar to merge sort but is more space optimized as we try to sort the elements of the list in place
"""
Algorithm:
    1. In quick sort, we call quick_sort on the list 
    2. Then, we get the position of the pivot element from calling quick sort
    3. We than call quick_sort on the sub list to the left and to the right of the pivot element, seperately
    4. In the quick_sort function, we:
        - Select a pivot element (in this case, the last index element)
        - Select two other reference points, one at the first index of the list and one before the pivot element
        - We start comparing all element in the reference indexes with the pivot element
            > If the left index is less than pivot we add one to it. If not, we check right index
            > If the right index is greater than pivot we subtract one from it
            > If left is greater and right is less than, we swap positions of left and right
            > Up until left and right index are at same position
            > At this point, swap pivot and the number because it would be greater than pivot
    NOTE: We do not create a seperate list when sorting. Instead, we pass the start end and index of the same list to the
            quick_sort function
"""

def quick_sort(arr, start, end):
    pivot = end
    l , r = start, end - 1
    while l < r:
        if arr[l] < arr[pivot]:
            l += 1
        elif arr[r] > arr[pivot]:
            r -= 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
    if arr[l] > arr[pivot]:
        arr[l], arr[pivot] = arr[pivot], arr[l]
        return l
    return pivot
    

def call_quick_sort(arr, left, right):
    if right == None:
        right = len(arr) - 1
        left = 0

    if left < right:
        pivot = quick_sort(arr, left, right)
        call_quick_sort(arr, left, pivot -1)
        call_quick_sort(arr, pivot+1, right)
    
b = list(range(2000))
random.shuffle(b)
print("BEFORE:: ", b)

call_quick_sort(b, 0, None)

print("AFTER:: ", b)
