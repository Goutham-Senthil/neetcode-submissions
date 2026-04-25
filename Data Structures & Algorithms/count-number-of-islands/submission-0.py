class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        R = len(grid)
        C = len(grid[0])

        def dfs(r,c):
            if (r<0 or r>=R or c<0 or c>=C or grid[r][c]!='1'):
                return

            grid[r][c] = '0'

            for r_off,c_off in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(r+r_off,c+c_off)

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1":
                    islands+=1
                    dfs(i,j)
        
        return islands