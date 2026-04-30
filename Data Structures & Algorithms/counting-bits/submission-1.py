class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0]*(n+1)

        for i in range(1,n+1):
            if i == 1:
                res[i] = 1
                continue
            if (i&(i-1)) == 0:
                res[i] = 1
            else:
                a_number = i&-i
                res[i] = res[a_number] + res[i-a_number]
        
        return res