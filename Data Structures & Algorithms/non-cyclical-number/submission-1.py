class Solution:
    def isHappy(self, n: int) -> bool:

        def happyMaker(n):
            digit = 0
            while n:
                digit += (n%10)**2
                n//=10
            return digit
        
        visted = set()

        while n!=1:
            n = happyMaker(n)
            if n in visted:
                return False
            visted.add(n)
            print(n)

        return True