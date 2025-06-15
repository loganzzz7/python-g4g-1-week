# problem:
# given an int arr nums -> ret all triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0
# i != j != k
# cannot contain dups and ans can be returned in any order
# 
# O(n) soln:
# iterate over i and for each i do twosum II soln -> 
# sorted arr
# two ptrs -> one at left one at right
# if nums[i] + nums[j] + nums[k] < 0 -> this means that nums[j] + nums[k] < nums[i]
#   therefore => inc j pointer to make nums[j] + nums[k] greater
# else:
#   dec k pointer to make nums[j] + nums[k] smaller
# to avoid dups -> need to inc num if i > 0 and nums[i] == nums[i - 1]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for index, val in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1
            while left < right:
                threesum = val + nums[left] + nums[right]
                if threesum < 0:
                    # need to inc j
                    left += 1
                elif threesum > 0:
                    right -= 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result