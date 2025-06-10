# soln:
# naive:
# for every value, iterate over everyother value and check if dup exists O(n^2) worst case runtime
# optimal:
def contains_dup(nums: list[int]) -> bool:
    visited = set()
    for num in nums:
        if num in visited:
            return True
        else:
            visited.add(num)
    return False