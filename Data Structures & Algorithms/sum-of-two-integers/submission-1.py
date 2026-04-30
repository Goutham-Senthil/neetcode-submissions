class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        c = 0
        c_bit = 0
        carry = 0
        for i in range(32):
            a_bit = (a>>i)&1
            b_bit = (b>>i)&1
            
            c_bit = carry ^ a_bit ^ b_bit
            if c_bit:
                c = c|(1<<i)

            # 1 + 1 + 1
            if (a_bit and b_bit) or (carry and a_bit) or (carry and b_bit):
                carry = 1
            else:
                carry = 0
        if c>= 2**31:
            c-=2**32
        
        return c