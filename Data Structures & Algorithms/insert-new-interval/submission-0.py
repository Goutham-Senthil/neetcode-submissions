class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        intervals.sort()

        prev_start , prev_end = intervals[0]

        res = [[prev_start,prev_end]]

        for i,(start,end) in enumerate(intervals):
            if i == 0:
                continue
            if start<=prev_end:
                res.pop()
                start_to_put = min(prev_start,start)
                end_to_put =  max(prev_end,end)
                res.append([start_to_put,end_to_put])
                prev_start = start_to_put
                prev_end = end_to_put
            else:
                res.append([start,end])
                prev_start = start
                prev_end = end
        
        return res