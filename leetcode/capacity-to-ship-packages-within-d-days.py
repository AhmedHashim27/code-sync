class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        l , r = max(weights), sum(weights)

        res = r
        def canship(cap):
            ships, curr = 1, cap
            for w in weights:
                if curr - w <0:
                    ships+= 1
                    curr = cap
                curr -= w
            return ships <= days



        while l <= r:
            cap = (l + r ) // 2
            if canship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res