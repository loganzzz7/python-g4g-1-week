# problem:
# given a string s -> return true if is palindrome
# otherwise -> ret false
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# 
# O(n) soln:
# use two pointers
# if left or right is non alpha num char -> inc pointer till it is alphanum char
# need one method to iterate through the string s 
# need another method to check if is alnum

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while r > l and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def isalnum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))