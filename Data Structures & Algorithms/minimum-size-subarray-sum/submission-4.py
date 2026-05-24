class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        mini = n =len(nums)
        summ = 0
        possible_sum = sum(nums)
        if possible_sum < target:
            return 0
        for r in range(n):
            summ+=nums[r]
            while summ >= target:
                mini = min(mini,r-l+1)
                summ-=nums[l]
                l+=1
        return mini