class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this is a 
        # binary search 
        # problem 
        # maximize minimize problem
        l = 1
        r = max(piles)
        res = r

        def can(time):
                summ = 0
                for p in piles:
                        summ+= math.ceil(p/time)
                        if summ >h:
                                return False
                return True
                
        while l<r:

                mid = (l+r)//2

                if can(mid):
                        res = mid
                        r = mid
                else:
                        l = mid+1

        return res
