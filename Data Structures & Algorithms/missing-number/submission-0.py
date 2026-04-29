class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        prev = 0
        nums.sort()
        for n in nums:
            if n != prev:
                return prev
            prev+=1
        return prev