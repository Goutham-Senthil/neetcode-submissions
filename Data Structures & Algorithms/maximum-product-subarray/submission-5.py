class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        currMin = 1
        currMax = 1

        for n in nums:
            if n == 0:
                currMin = 1
                currMax = 1
                continue
            oldcurrMax = n*currMax
            currMax = max(n*currMax,n*currMin,n)
            currMin = min(oldcurrMax,n*currMin,n)
            res = max(currMax,res)
            print(f"{currMax} and {currMin} and {res} and {n}")
        return res