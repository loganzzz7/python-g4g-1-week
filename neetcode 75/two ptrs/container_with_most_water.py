# problem:
# given an int array of heights where height[i] represents the height of the i-th bar
# choose any two bars as containers
# return bars that allow for max water to be contains
# water contained = min(height[l], height[r]) * height[r] - height[l]
# 
# O(n) soln:
# two ptrs
# l = 0
# r = len(arr) - 1
# most = 0
# while l < r:
#   # width * height
#   area = (r - l) * min(heights[l], heights[r])
#   most = max(most, area)
#   if heights[l] <= heights[r]:
#   # want to be able to find the max two heights so keep largest and iterate to find second largest
#       l += 1
#   else:
#       r -= 1
# return largest

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l = 0
        r = len(heights) - 1
        most = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            most = max(most, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return most