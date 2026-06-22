class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        numsset = set(nums)

        return len(numsset) != len(nums)