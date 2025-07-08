# problem:
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
# 
# soln:
# recursive dfs
# keep a list of visited cells
# basecase: 
# avoid visited cells; boundary check, value check
# recursively check every direction -> up, down, l, r
# 
# implementation:
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()
        
        def dfs(r, c, i):
            # base case: if i reaches end of word then it is found
            if i == len(word):
                return True
            # base case: stop case
            if (r < 0 or c < 0 or
                r > row - 1 or c > col - 1 or
                board[r][c] != word[i] or
                (r, c) in visited):
                return False
            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res
        for r in range(row):
            for c in range(c):
                if not dfs(r, c, 0):
                    return False
        return True