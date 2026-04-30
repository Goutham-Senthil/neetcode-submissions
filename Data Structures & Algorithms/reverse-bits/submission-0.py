class Solution:
    def reverseBits(self, n: int) -> int:

        res = 0

        for i in range(32):
            # shift it to the right
            bit = (n>>i)&1
            # logic OR it with the bit at that position
            res = res | (bit<<31-i)
        
        return res