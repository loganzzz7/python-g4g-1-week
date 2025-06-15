# problem:
# given string s -> find length of longest substring without dup chars
# e.g. 
# s = "zxyzxyz"
# output = "3"
# 
# O(n) soln:
# slide window tech
# l = 0
# charset = set()
# longest = 0
# iterate through r
# if next char causes a dup:
#   subtract from left until no dup
# else:
#   add r to set
# longest = max(longest, window == r - l + 1)
# return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charset = set()
        longest = 0
        
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            longest = max(longest, (r - l + 1))
        return longest