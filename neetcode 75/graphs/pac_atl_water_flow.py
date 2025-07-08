# problem:
# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
# The Pacific Ocean touches the island's left and top edges, 
# and the Atlantic Ocean touches the island's right and bottom edges.
# 
# The island is partitioned into a grid of square cells. 
# You are given an m x n integer matrix heights where heights[r][c] represents 
# the height above sea level of the cell at coordinate (r, c).
# 
# The island receives a lot of rain, and the rain water can flow to neighboring cells 
# directly north, south, east, and west 
# if the neighboring cell's height is less than or equal to the current cell's height. 
# Water can flow from any cell adjacent to an ocean into the ocean.
# 
# Return a 2D list of grid coordinates result where 
# result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to 
# both the Pacific and Atlantic oceans.
# 
# soln:
# start from edges and traverse inwards
# find cells that can reach pacific and find cells that can reach atl
# return the intersection of those two sets of cells
# use a recursive dfs
# 
# implementation:
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowl = len(heights)
        coll = len(heights[0])
        pac = set()
        atl = set()
        res = []
        
        def dfs(r, c, visited, prevHeight):
            if (r < 0 or c < 0 or
                r > rowl - 1 or c > coll -1 or
                heights[r][c] < prevHeight or
                (r, c) in visited):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
        
        for r in range(rowl):
            # left
            dfs(r, 0, pac, heights[r][0])
            # right
            dfs(r, coll - 1, atl, heights[r][coll - 1])
        
        for c in range(coll):
            # top
            dfs(0, c, pac, heights[0][c])
            # bot
            dfs(rowl - 1, c, atl, heights[rowl - 1][c])
        
        for r in range(rowl):
            for c in range(coll):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res