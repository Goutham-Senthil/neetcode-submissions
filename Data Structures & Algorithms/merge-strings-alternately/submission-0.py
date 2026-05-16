class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = ''
        for c1,c2 in zip_longest(word1,word2):
            if c1 and c2:
                res += c1+c2
            elif not c1:
                res += c2
            else:
                res += c1
        
        return res