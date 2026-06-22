class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)

        for i in range(1,n:=len(nums)):
            prefix[i] *= nums[i-1] * prefix[i-1]

        for i in range(n-2,-1,-1):
            postfix[i] *= nums[i+1] * postfix[i+1]
        
        for i in range(n):
            prefix[i] *= postfix[i]
        
        return prefix