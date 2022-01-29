import random
# Implementing merge sort in python
"""
Algorithm::
    1. Split list into two parts and call merge_sort on both sub parts parts: Recursive
    2. Continue this until the rightmost pointer is no longer greater than the leftmost
    3. When we have single elements, return what we have 
    4. on return perform a special merging and sorting operation which combines both return array and:
        - compare elements of the two returned subset against one another and transfer the lesser of both
            to a new list
        - when the items in one list is exhausted, completely transfer all items in the other list to the new list
"""

# def merge(left, right):
#     merge_list = []
#     i, j = 0, 0 
#     # i is for left list, j is for right list
#     for _ in range(len(left) + len(right)):
#         if len(left) > i and len(right) > j:
#             if left[i] < right[j]:
#                 merge_list.append(left[i])
#                 i += 1
#             else:
#                 merge_list.append(right[j])
#                 j += 1
#         else:
#             merge_list += left[i:] + right[j:]
#             break
#     return merge_list

def merge(left, right):
    merge_list = []
    i, j = 0, 0 
    # i is for left list, j is for right list
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1
    
    merge_list += left[i:] + right[j:]
    return merge_list

def merge_sort(arr):
    l, r = 0, len(arr) - 1
    mid = len(arr) // 2
    if l < r:
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    else:
        return arr


b = list(range(30))
random.shuffle(b)
print("BEFORE: ", b)

sorted_arr = merge_sort(b)
print("AFTER: ", sorted_arr)

