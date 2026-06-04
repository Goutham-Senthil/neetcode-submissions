class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0

        res = []
        i = len(a) - 1
        j = len(b) -1
        while i>=0 or j>=0 or carry:
            a_digit = int(a[i]) if i>=0 else 0
            b_digit = int(b[j]) if j>=0 else 0
            
            summ = a_digit + b_digit + carry
            res_to_append = (summ)%2
            print(summ)
            if summ >= 2:
                carry = 1 # idk 
            else:
                carry = 0

            res.append(str(res_to_append))
            i-=1
            j-=1
        
        return "".join(res)[::-1]