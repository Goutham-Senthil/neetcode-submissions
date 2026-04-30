class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        stack = []
        count = 0
        n = len(intervals)

        intervals.sort(key = lambda x:x[0])

        prevStart, prevEnd = intervals[0]
        
        for i in range(1,n):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                count+=1
                prevEnd = min(intervals[i][1],prevEnd)

        return count