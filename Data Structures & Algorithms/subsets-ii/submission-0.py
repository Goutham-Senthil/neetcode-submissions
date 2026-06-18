class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        # keep all same elements near each other
        nums.sort()


        def f(tmp,index):
            if index == (n:=len(nums)):
                # we want a subset ending at EACH index
                res.append(tmp[::])
                return 
            
            tmp.append(nums[index])
            f(tmp,index+1) # 0-indexed
            tmp.pop()
            # within bounds and is a duplicate
            while index+1 < n and nums[index+1] == nums[index]:
                index+=1
            
            f(tmp,index+1)
        
        f([],0)
        return res
