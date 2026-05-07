class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_res = 0
        count = 0

        for num in nums:
            if num:
                count+=1
                max_res = max(max_res,count)
            else:

                count = 0
        # max_res = max(max_res,count)
        return max_res