# soln: O(n)
# something is an anagram of something else if they have the same letters -> god and dog or racecar and carrace
# we need to track the number of each character that a string has 
# and if two strings have the same count for the characters then they are anagrams

def valid_anagram(s: str, t: str) -> bool:
    # anagrams must be of the same length!
    if len(s) != len(t):
        return False
    
    # track count of the two strings with hashtables
    # match letter to count
    count_s = {}
    count_t = {}

    for i in range(len(s)):
        # at letter s[i] -> track count
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    
    # if the two strings have the same count of each letter then they are anagrams
    return count_s == count_t