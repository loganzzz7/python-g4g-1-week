# problem:
# Design a data structure that supports adding new words and 
# finding if a string matches any previously added string.
# 
# Implement the WordDictionary class:
# 
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
# 
# soln:
# use a Trie struct again
# every node has children list and eow
# same logic for add word 
# search logic -> "." matches with every char
# when it is "." go down the children list -> inc i pointer of word by 1
# therefore use a recursive dfs to check
# 
# implementation:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        def dfs(index, node):
            
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child): # if the next character following . matches with a child
                            return True
                    return False # if the next char following all the . doesn't match then ret false
                else:
                    if c not in node.children:
                        return False
            return node.eow
        return dfs(0, curr)