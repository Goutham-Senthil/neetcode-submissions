class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def f(tmp,open_count,closed_count):
            if len(tmp) == 2*n:
                res.append("".join(tmp))
                return

            if open_count < n:
                tmp.append('(')
                f(tmp,open_count+1,closed_count)
                tmp.pop()
            if closed_count < open_count:
                tmp.append(')')
                f(tmp,open_count,closed_count+1)
                tmp.pop()
        
        f([],0,0)
        return res
