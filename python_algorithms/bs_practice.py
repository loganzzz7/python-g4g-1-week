# Binary Search
# Pseudo-code =>
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
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] > target:
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#     else:
#         return f"{target} is not in array {arr}"
    
# print(binary_search(sorted(a), 30))

# PRACTICE 05/22/2025
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         if arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not in {arr}"

# print(binary_search(sorted(a), 28))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not in {arr}"

# print(binary_search(sorted(a), 8))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not in {arr}"
    
# print(binary_search(sorted(a), 3))

# PRACTICE 05/23/2025
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(binary_search(sorted(a), 12))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found"
    
# print(binary_search(sorted(a), 20))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(binary_search(sorted(a), 12))

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(binary_search(sorted(a), 12))

# PRACTICE 05/24/2025
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(binary_search(sorted(a), 121))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(bs(sorted(a), 12))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(bs(sorted(a), 12))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return f"{target} is found"
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} is not found in {arr}"
    
# print(bs(sorted(a), 12))
# print(bs(sorted(a), 120))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return "not found"
    
# print(bs(sorted(a), 121))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] > target:
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#     else:
#         return f"{target} not found"
    
# print(bs(sorted(a), 12))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} not found"

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] > target:
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#     else:
#         return f"{target} not found in {arr}"
    
# print(bs(sorted(a), 121))

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] > target:
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#     else:
#         return f"{target} not found"

# def bs(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return target
#         elif arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#     else:
#         return f"{target} not found in {arr}"

def bfs(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    else:
        return f"{target} is not found in {arr}"

print(bfs(sorted(a), 121))

