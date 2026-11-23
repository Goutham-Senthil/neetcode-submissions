class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort
        nums.sort()
        x = len(nums)
        for i,n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            L = i+1
            R = x - 1

            while L < R:
                tS = n + nums[L] + nums[R]

                if tS < 0:
                    L += 1
                elif tS > 0:
                    R -= 1
                else:
                    res.append([n,nums[L],nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return res