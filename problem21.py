'''Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start_times=sorted[i.start for i in intervals];
        end_times=sorted[i.end for i in intervals];
        res,count=0,0
        s,e=0,0
        while s<len(intervals):
            if(start_times[s]<end_times[e]):
                s=s+1
                count=count+1
            else:
                e=e+1
                count=count-1
            res=max(res,count)
        return res
        # Write your code here
