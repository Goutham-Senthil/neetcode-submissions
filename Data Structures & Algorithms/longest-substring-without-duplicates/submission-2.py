class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        strset = set()  
        window = 0
        n = len(s)

        for r in range(n):
            while s[r] in strset:
                strset.remove(s[l])
                l+=1
            strset.add(s[r])
            window = max(window,(r-l+1))
        return window