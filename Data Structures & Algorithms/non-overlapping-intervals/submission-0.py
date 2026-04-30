class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        stack = []
        count = 0
        n = len(intervals)

        intervals.sort(key = lambda x:x[0])
        
        for i in range(n):
            if not stack:
                stack.append(intervals[i])
            else:
                if intervals[i][0] < stack[-1][1]:
                    stack[-1][1] = min(stack[-1][1],intervals[i][1])
                else:
                    stack.append(intervals[i])


        return n-len(stack)