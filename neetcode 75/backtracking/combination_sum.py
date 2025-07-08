# problem:
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# 
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# 
# The test cases are generated such that the number of unique combinations that sum up to target 
# is less than 150 combinations for the given input.
# 
# soln: we are looking for combinations not permutations -> [2, 3] and [3, 2] == same
# use a recursive soln
# a decision tree with len(candidates) number of nodes
# for each node, left path includes parent val and right path doesn't
# this avoids permutations
# when left branch sum > target, go to right branch
# use i pointer to track candidate and shift i pointer when split branch
# 
# implementation:
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i > len(candidates) - 1 or total > target:
                return
            # split left: include candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            # split right: exclude candidates[i]
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, [], 0)
        return res