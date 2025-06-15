# problem:
# given string s consisting of ONLY UPPER CASE letters and int k
# can replace up to k characters in string s
# return length of longest substring which contains only one char
# 
# O(n) soln:
# sliding window tech
# l = 0
# longest = 0
# iterate through r
# while window length (r - l + 1) - most freq char > k:
#   # not a valid soln anymore ->
#   inc left pointer until valid again
#   l += 1
# longest = max(longest, (r - l + 1))
# return longest

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        longest = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, (r - l + 1))
        return longest