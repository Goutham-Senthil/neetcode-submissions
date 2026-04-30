"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])

        res , count = 0,0
        n = len(intervals)
        s_pointer = 0
        e_pointer = 0

        while s_pointer<n:
            if start[s_pointer]<ends[e_pointer]:
                s_pointer+=1
                count+=1
            else:
                count-=1
                e_pointer+=1
            res = max(res,count)
        
        return res
