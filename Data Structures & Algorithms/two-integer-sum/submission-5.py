class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        h = {}

        for i,x in enumerate(nums):
            y = target - x
            if y in h:
                return [h[y],i]
            h[x] = i

        return [-1,-1] 