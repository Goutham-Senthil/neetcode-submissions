class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(candidates)
        candidates.sort()
        
        def f(i,tmp):
            if sum(tmp) == target:
                res.append(tmp[::])
                return
            
            if sum(tmp) > target or i >= n:
                # oops
                return
            
            
            tmp.append(candidates[i])
            f(i+1,tmp)
            tmp.pop()
            while i+1 < n and candidates[i] == candidates[i+1]:
                i+=1
            f(i+1,tmp)
        
        f(0,[])
        return res
            
