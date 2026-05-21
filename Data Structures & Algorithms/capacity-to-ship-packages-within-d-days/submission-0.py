class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = 501*50_000

        def possible(max_weight):
            day = 1
            currCap = 0

            for w in weights:
                if currCap + w <= max_weight:
                    currCap+=w
                else:
                    currCap = 0
                    currCap+=w
                    day +=1
                if day > days:
                    return False
            return True



        while l <= r:
            mid = (l+r)//2

            if possible(mid):
                res = min(res,mid)
                r = mid -1
            else:
                l = mid+1
        return res