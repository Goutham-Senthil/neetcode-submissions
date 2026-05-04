class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_split = s.strip().split(' ')
        
        print(s_split)
        return len(s_split[-1])