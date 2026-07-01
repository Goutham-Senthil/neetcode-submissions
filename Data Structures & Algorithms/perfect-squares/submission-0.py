class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        # worst case its a sum of "n" ones
        dp[0] = 0

        for i in range(1,n+1):

            for s in range(1,i):
                if (s*s) > i:
                    break
                target = i - (s*s)
                dp[i] = min(dp[i],1+dp[target])
            
        return dp[-1]