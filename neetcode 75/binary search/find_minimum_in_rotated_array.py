# problem:
# given an array of length n which was originally sorted in ascending order
# it has now been rotated between 1 and n times
# assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array
# O(n) answer is trivial => must use O(lgn) soln
# 
# O(lgn) soln:
# BINARY SEARCH!
# every step reduce searched arr logarithmically => O(logn) rt
# result = 0
# l = 0
# r = len(nums) - 1
# while l <= r:
#   if nums[l] < nums[r]:
#       return nums[l]
#   mid = (l + r) // 2
#   result = min(result, nums[mid])
#   if nums[l] <= nums[mid]:
#       # in left half of the arr -> search right
#       l = mid + 1
#   else:
#       # in right half of the arr -> search left
#       r = mid - 1
# return result

class Solution:
    def findMin(self, nums: list[int]) -> int:
        result = float("infinity")
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                # is alr sorted
                result = min(nums[l], result)
                break
            
            mid = (l + r) // 2
            result = min(result, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return result