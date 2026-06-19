class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        resset = set()
        def f(tmp,prev_chosen):
            if len(tmp) == len(nums):
                resset.add(tmp[::])
                return
            

            for i,num in enumerate(nums):
                if i not in prev_chosen:
                    nwtmp = tmp + (num,)
                    prev_chosen.add(i)
                    f(nwtmp,prev_chosen)
                    prev_chosen.remove(i)

            
        f(tuple(),set())
        return [list(x) for x in resset]