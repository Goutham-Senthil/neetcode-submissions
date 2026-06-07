class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
        carry = 0
        for i in reversed(range(n)):

            if digits[i]<9:
                digits[i]+=1
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
        
        if carry:
            digits = [1] + digits
        
        return digits