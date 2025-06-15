# problem:
# given strings s and t =>
# return the shortest substring of s such that every character in t, including duplicates, is present in the substring. 
# If such a substring does not exist, return an empty string "".
# 
# O(n) soln:
# sliding window tech!
# l = 0
# iterate r:
# when have == need:
# subtract l until condition no longer met
# this will be a valid sequence
# update length if this sequence shorter than prev sequence
# use l and r pointers to return final ans
# perform two checks -> one for does each char in t meet; other for does overall chars in t meet

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window = {}
        count = {}

        for char in t:
            count[char] = 1 + count.get(char, 0)
        
        have = 0
        need = len(count)

        result = [-1, -1]
        reslen = float("infinity")

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < reslen:
                    reslen = (r - l + 1)
                    result = [l, r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = result

        return s[l:r+1] if reslen != float("infinity") else ""