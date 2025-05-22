# Binary Search
# => performed on a SORTED array
# while left <= right:
# One: compare target against middle elt
# Two: if target > middle:
#           middle becomes right middle
#           compare target with right middle
    #  else:
#           middle becomes left middle
#           compare target with left middle
# runtime: O(logn); this is log time because the searched array gets halved every time

# e.g. =>
a = [10, 12, 3, 5, 6, 75, 18, 9]

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2 # // to do floor division
#         if arr[mid] == target: # found
#             return target
#         elif arr[mid] < target: # target is smaller than mid so search left side
#             left = mid + 1
#         elif arr[mid] > target: # target is larger than mid so search right side
#             right = mid - 1
#     else:
#         return f"{target} is not in array"
        
# print(binary_search(sorted(a), 21))

# PRACTICE 05/21/2025
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
    else:
        return f"{target} is not in array {arr}"
    
print(binary_search(sorted(a), 30))