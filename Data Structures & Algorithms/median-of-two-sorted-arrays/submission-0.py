class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:

        if len(B) < len(A):
            A,B = B,A
        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1
        while True:
            i = (l+r)//2
            j = half-i-2

            Aleft = A[i] if i>=0 else float('-inf')
            Aright = A[i+1] if (i+1)<len(A) else float('inf')
            Bleft = B[j] if j>=0 else float('-inf')
            Bright = B[j+1] if (j+1)<len(B) else float('inf')    

            # if success
            if Aleft<=Bright and Bleft<=Aright:
            
                res = min(Aright,Bright)
                if total%2 == 0:
                    res = (res+max(Aleft,Bleft))/2 
                return res
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1 