class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def is_alpha(c):
            return (ord('a') <= ord(c) <= ord('z')) or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9')
        
        l = 0
        r = len(s) - 1
        while l < r:
            while l < len(s) and l < r and not is_alpha(s[l]):
                l+=1
            while r > -1 and l < r and not is_alpha(s[r]):
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                print(f"{s[l]} == {s[r]}")
            l+=1
            r-=1
        return True