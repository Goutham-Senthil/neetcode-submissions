class Solution:
    def isValid(self, s: str) -> bool:
        

        mapper = {
                    "[" :"]",
                    "{" : "}",
                    "(" : ")"
        }
        stack = []
        for b in s:
            if b in mapper.keys():
                stack.append(b)
            else:
                if stack and mapper[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
        return not stack