class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c!=']':
                stack.append(c)
            else:
                substr = ''
                while stack[-1]!='[':
                    substr = stack.pop() + substr
                stack.pop()
                # the number
                val = ""
                while stack and stack[-1].isdigit():
                    val = stack.pop() + val
                stack.append(int(val)*substr)
        return ''.join(stack)