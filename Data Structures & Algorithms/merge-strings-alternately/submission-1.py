class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        for c1,c2 in zip_longest(word1,word2):
            if c1 and c2:
                res.append(c1+c2)
            elif not c1:
                res.append(c2)
            else:
                res.append(c1)
        
        return ''.join(res)