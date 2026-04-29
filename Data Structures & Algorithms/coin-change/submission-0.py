class Solution:
    def coinChange(self, coins: List[int], n: int) -> int:

        dp = [0]*(n+1)

        for i in range(1,n+1):
            mini = float('inf')
            for coin in coins:
                diff = i-coin
                if diff<0:
                    break
                mini = min(dp[diff]+1,mini)
            dp[i]=mini
        
        return dp[n] if dp[n]<float('inf') else -1