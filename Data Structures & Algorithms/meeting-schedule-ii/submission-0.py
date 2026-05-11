"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        res = 0
        heapq.heapify(rooms)
        intervals.sort(key=lambda x: x.start)

        for i in intervals:
            if len(rooms) and rooms[0] <= i.start:
                heapq.heappop(rooms)

            heapq.heappush(rooms, i.end)
            res = max(res, len(rooms))
        return res