# There is an integer array nums sorted in ascending order (with distinct values).
# 
# Prior to being passed to your function, nums is possibly rotated at an 
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# Soln O(lgn):
# idea: since we must write an O(lgn) soln it must be binary search
# we need to figure out which section of the arr mid is in
# if mid is in the left half -> then check target against left and mid:
#   if the target is greater than mid or less than left:
#       search right
#   else:
#       search left
# else:
#   if the target is lesser than mid or greater than right:
#       search left
#   else:
#       search right
# return -1 if not found or else return mid
# 
# implementation:
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1