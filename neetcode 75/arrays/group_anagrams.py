# problem:
# for an array of words, return an array of anagram arrays
# soln: O(n)
# we track count of every since word
# since there are only 26 characters, we can use an array of [0] * 26 to map each word

from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    result = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
            # we use ascii to index =>
            # a - a = 0
            # b - a = 1
            # ... this indexes correctly for the count array
        # result will use count as the keys and words as the values
        # keys must be immutable so use tuple
        # this appends the words with the same counts to the same key
        result[tuple(count)].append(word)
    # we only want to return the values of the dict which are arrays of words that are anagrams
    return list(result.values())