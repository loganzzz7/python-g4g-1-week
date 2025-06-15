# problem:
# input arr is 1-indexed and sorted
# find two numbers that sum to the target
# return indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# 
# O(n) soln:
# two ptrs
# l = 0
# r = len(arr) - 1
# if nums[l] + nums[r] < target:
#   inc left
# else:
#   dec right
# return [l + 1, r + 1]

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        
        return [l + 1, r + 1]