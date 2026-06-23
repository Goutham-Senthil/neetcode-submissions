class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = prices[0]
        profit = 0
        for p in prices[1:]:
            profit = max(p-minPrice,profit)
            minPrice = min(minPrice,p)
        return profit
            