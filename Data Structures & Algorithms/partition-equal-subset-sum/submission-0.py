class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        if target%2:
            return False
        
        target//=2

        dp = set()
        dp.add(0)
        for num in nums:
            currset = set()
            for val in dp:
                currset.add(val)
                currset.add(num+val)
            dp = currset
        
        return target in dp
