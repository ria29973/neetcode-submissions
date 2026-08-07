"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, 0))
        times.sort()
        needed = 0
        cur = 0
        for time, t in times:
            if t == 1:
                cur+=1
                needed = max(needed, cur)
            else:
                cur-=1
        return needed

        
                
