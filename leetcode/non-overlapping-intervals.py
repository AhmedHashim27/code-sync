class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        if not intervals:
            return 0

        intervals.sort(key = lambda x:x[1])
        end = float("-inf")
        removals = 0


        for s, e in intervals:
            if s >= end:
                end = e

            else:
                removals += 1
        return removals