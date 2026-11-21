class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        mx = 0
        for n in nums:

            if n-1 not in nums_set:
                count = 0
                while n in nums_set:
                    count += 1
                    n += 1
                mx = max(count,mx)
        
        return mx
