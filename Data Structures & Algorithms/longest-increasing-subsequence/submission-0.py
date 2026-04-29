class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # inutuion 
        # longest subsequence we can make
        # if we end here
        n = len(nums)
        dp = [1]*(n) # by default we can make one only


        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])
        
        return max(dp)

