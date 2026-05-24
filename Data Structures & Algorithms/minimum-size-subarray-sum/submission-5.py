class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        mini = 100_001
        summ = 0

        for r in range(n):
            summ+=nums[r]
            while summ >= target:
                mini = min(mini,r-l+1)
                summ-=nums[l]
                l+=1
        return mini if mini < 100_001 else 0