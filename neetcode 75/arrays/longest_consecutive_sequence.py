# problem:
# given an array of ints => return the length of the longest consecutive sequence of elts that can be formed
# the elts do not have to be consecutive in the original array
# 
# O(n) soln:
# convert array of int into a set
# iterate the set, if there is no left neighbour in the array (num - 1) then treat it as the start of a sequence
# for each sequence, check if there is a right neighbour (num + 1):
# if so inc length of sequence
# at the end of every sequence, update the longest length
# return the longest

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        numset = set(nums)

        for num in numset:
            if (num - 1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length)
        return longest