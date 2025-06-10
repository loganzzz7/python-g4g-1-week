# problem:
# given an array of ints, return an array where each val is the product of the given array except itself
# e.g.
# [1, 2, 3, 4] -> [2*3*4, 1*3*4, 1*2*4, 1*2*3]
# soln: O(n)
# we use a prefix and suffix
# prefix contains the result of the numbers before the current multiplied together
# suffic contains the result of the numbers after the current multiplied together

def product_of_arr_except_self(nums: list[int]) -> list[int]:
    result = [0] * len(nums) # -> result is the same length as the given array
    
    prefix = 1 # -> prefix defaults to 1 if there is no prefix since 1 * anything = itself
    # prefix -> traverse from left to right
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]
    
    suffix = 1 # -> suffix defaults to 1 if there is no suffix
    # -> traverse from right to left: start at -1 index so end of array; go until -1 (EXCLUSIVE) so go until 0; -1 reverse order
    for i in range(len(nums) - 1, -1, -1):
        # result[i] currently contains prefix so we multiply itself with the suffix
        result[i] *= suffix
        suffix *= nums[i]
    
    return result