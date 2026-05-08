class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                value = stack.pop()
                stack.append(value)
                stack.append(value*2)
            elif op == "+":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(value2)
                stack.append(value1)
                stack.append(value1+value2)
            else:
                stack.append(int(op))
        return sum(stack)