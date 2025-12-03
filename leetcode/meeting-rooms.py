class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True

        intervals.sort(key = lambda x : x[0])

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            previousEnd = intervals[i-1][1]

            if start < previousEnd:
                return False

        return True