class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [0]*(n+1)

        # dp[1] = cost[0]
        # dp[2] = min(cost[1],cost[0])


        for i in range(2,n+1):
            dp[i] = min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1])
        print(dp)
        return dp[-1]