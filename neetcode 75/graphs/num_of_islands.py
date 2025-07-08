# problem:
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.
# 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
# 
# soln:
# backtracking bfs
# mark all neighbours as visited => traverse until all are visited
# 
# implementation:
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs soln
        if not grid:
            return 0
        
        visited = set()
        row = len(grid)
        col = len(grid[0])
        
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            
            while len(queue) > 0:
                r, c = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(row) and
                        nc in range(col) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                
        # go thru each cell -> do a bfs when a cell = 1 to add all the 1 cells to the visited set
        # repeat until all 1 blocks are visited and each 1 block is an island
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands