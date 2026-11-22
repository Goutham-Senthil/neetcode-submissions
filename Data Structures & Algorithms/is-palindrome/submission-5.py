class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        L = 0
        R = n - 1

        def valid(c):

            return (
                ('a' <= c <= 'z') or
                ('A' <= c <= 'Z') or
                ('0' <= c <= '9') 
            )

        while L <= R:

            while L < R and not valid(s[L]):
                L += 1
            while R > L and not valid(s[R]):
                R -= 1
            
            # if s[L].isnumeric() and s[R].isnumeric() and s[L] != s[R]:
            #     return False
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True