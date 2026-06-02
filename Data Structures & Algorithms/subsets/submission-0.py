class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def f(i):
            if i>=len(nums):
                res.append(subset[::])
                return 
            subset.append(nums[i])
            f(i+1)
            subset.pop()
            f(i+1)
        f(0)
        return res