class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def f(tmp,prev_chosen):
            if len(tmp) == len(nums):
                res.append(tmp[::])
                return
            

            for num in nums:
                if num not in prev_chosen:
                    tmp.append(num)
                    prev_chosen.add(num)
                    f(tmp,prev_chosen)
                    prev_chosen.remove(num)
                    tmp.pop()
        
        f([],set())
        return res