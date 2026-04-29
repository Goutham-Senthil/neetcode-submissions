class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = (n*(n+1))//2
        print(res)
        for n in nums:
            res-=n
        return res