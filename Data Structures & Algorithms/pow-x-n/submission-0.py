class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        n_ = n
        n = abs(n)
        while n:
            if n & 1:
                res = (res * x)
            x =(x*x)
            n >>= 1
        return res if n_ >=0 else 1/res