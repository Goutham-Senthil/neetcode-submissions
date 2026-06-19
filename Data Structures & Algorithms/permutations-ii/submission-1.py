class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        resset = set()
        nums.sort()
        count = collections.Counter(nums)
        
        def f(tmp):
            if len(tmp) == len(nums):
                res.append(tmp[::])
                return
            
            for n in count.keys():
                if count[n] > 0:
                    tmp.append(n)
                    count[n]    -=1

                    f(tmp)

                    tmp.pop()
                    count[n] += 1

        f([])
        return res