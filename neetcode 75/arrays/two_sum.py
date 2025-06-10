# given an array of ints, find two values that sum to target
# naive soln: O(n^2)
# for each val, iterate over every other val and see if they add up to target
# two for loops so n^2

# optimal: O(n)
# use hashtable to track the values and indices of all ints in array and iterate over it once
# hashtable search takes constant O(1) time
# use a value to index table since we are returning the indices of the values that sum to target
# when we plug in target - current val = diff, we can use diff as an "index" into our table to get the actual index return

def two_sum(nums: list[int], target: int) -> list[int]:
    prevmap = {}

    for index, val in enumerate(nums):
        diff = target - val
        # walk from left to right -> if the diff has already been visited then it will have been stored into the hashtable
        # which means that we can use diff as "index" into the table
        if diff in prevmap:
            # if diff already in visited, it will come before current
            return [prevmap[diff], index]
        prevmap[val] = index