class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res = []

        def backtrack(start,lst):
            if sum(lst) == target:
                res.append(lst[::])
                return
            
            if lst and sum(lst) > target:
                return
            
            for i in range(start,len(nums)):
                lst.append(nums[i])
                backtrack(i,lst)
                lst.pop()        

        for i,num in enumerate(nums):
            backtrack(i,[num])


        return list(res)
