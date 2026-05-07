class Solution:
    def scoreOfString(self, s: str) -> int:
        a_value = ord('a')
        prev = ord(s[0]) - a_value

        summ = 0

        for c in s[1:]:
            curr = ord(c) - a_value
            summ += abs(curr-prev)
            prev = curr
        
        return summ