class Solution:
    def numDecodings(self, s: str) -> int:
        # this is a dp problem 

        # our base case is that we can make at least 
        # ONE substring
        n = len(s)

        dp = {n:1}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            # we cant really make a "valid" 
            # mapping if starting with 0
            if s[i]=="0":
                return 0
            
            res = dfs(i+1)

            if (i+1<len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            dp[i] = res
            return dp[i]
        
        return dfs(0)