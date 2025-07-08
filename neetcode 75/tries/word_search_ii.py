# problem:
# Given an m x n board of characters and a list of strings words, return all words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.
# 
# soln:
# map the list of words to a trie
# -> when going thru every cell to dfs -> match to trie
# -> if it is eow => add the word to the result list
# 
# implementation:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = {}
    
    def addWord(self, word):
        curr = self
        
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.chilren[c]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
        
        row = len(board)
        col = len(board[0])
        
        visited = set()
        res = set()
        
        def dfs(r, c, node, word):
            # Basecase:
            if (r < 0 or c < 0 or
                r > row - 1 or c > col - 1 or
                board[r][c] not in node.children or
                (r, c) in visited):
                return

            visited.add((r, c))
            node = node.children(board[r][c])
            word += board[r][c]
            
            if node.eow:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r, c))
        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")
        return list(res)