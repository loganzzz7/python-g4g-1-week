# problem:
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store 
# and retrieve keys in a dataset of strings. There are various applications of this data structure, 
# such as autocomplete and spellchecker.
# 
# Implement the Trie class:
# 
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), 
# and false otherwise.
# 
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word 
# that has the prefix prefix, and false otherwise.
# 
# soln:
# need to create a TrieNode class
# each TrieNode need to map to it's children
# each TrieNode need to have bool to determine if it is end of word
# search needs to check of end of word
# starts with just checks children
# 
# implementation:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.EOW = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.EOW

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)