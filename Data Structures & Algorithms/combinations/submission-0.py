class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def f(last,tmp,curr_k):
            if curr_k == k:
                res.append(tmp[::])
                return
            
            # we do not want to use last ?
            for i in range(last+1,n+1):
                tmp.append(i)
                f(i,tmp,curr_k+1)
                tmp.pop()
        
        f(0,[],0)
        return res