# problem:
# given an array of strings -> encode them some way then decode it back to the same string
# need to find good delimiters

# soln: O(n)
# e.g.
# ["love", "you"] -> "4#love3#you"
# use # as a delimiter -> number indicates how many chars need to be read after reading the delimiter

def encode(strs: list[str]) -> str:
    result = ""

    for str in strs:
        result += str(len(str)) + "#" + str
    return result

def decode(s: str) -> list[str]:
    result = []
    i = 0

    # read from start to end of inputted string
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j]) # -> start from i; end at j (EXCLUSIVE) -> read i
        result.append(s[j + 1:j + 1 + length]) # -> start from j + 1; j is currently on # and end after the length of the word
        # update i to be after the word
        i = j + 1 + length
    return result
