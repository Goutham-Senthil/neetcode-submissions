class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # this is a 
        # binary search 
        # problem 
        # maximize minimize problem
        l = 1
        r = max(piles)
        res = r

        def can(bph):
                time = 0
                for p in piles:
                        time+= math.ceil(p/bph)
                        if time >h:
                                return False
                return True
                
        while l<r:
                
                mid = (l+r)//2
                
                # this is our bannas per hour
                if can(mid):
                        res = mid
                        r = mid
                else:
                        l = mid+1

        return l
