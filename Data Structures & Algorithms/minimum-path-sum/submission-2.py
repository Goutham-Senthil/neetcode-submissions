class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[201]*n for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if j != 0:
                    dp[i][j] = min(dp[i][j-1] + grid[i][j],dp[i][j])
                if i != 0:
                    dp[i][j] = min(dp[i-1][j] + grid[i][j],dp[i][j])



        return dp[m-1][n-1]