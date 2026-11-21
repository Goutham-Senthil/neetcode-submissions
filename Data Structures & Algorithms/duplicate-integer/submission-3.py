class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nummset = set()


        for n in nums:
            if n in nummset:
                return True
            nummset.add(n)
        
        return False