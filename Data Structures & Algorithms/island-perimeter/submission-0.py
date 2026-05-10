class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        seen = set()
        
        def dfs(i,j):
            # out of bounds
            # or water
            if (i<0 or j<0 or i>=m or j>=n or grid[i][j]==0):
                return 1
            
            if (i,j) in seen:
                return 0
            seen.add((i,j))
            summ = 0
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                x = i+dx
                y = j+dy
                summ += dfs(x,y)
            return summ

        p = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    p = dfs(i,j)
                    return p
        return p