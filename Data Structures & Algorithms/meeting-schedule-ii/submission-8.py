"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        times = []
        for i in intervals:
            times.append((i.start, 1))
            times.append((i.end, 0))
        times.sort()
        cur = 0
        needed = 0
        for time, meetingType in times:
            if meetingType == 1:
                cur+=1
                needed = max(needed, cur)
            else:
                cur-=1
        return needed

        
       


        