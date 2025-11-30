class Solution(object):
    def maximumProfit(self, present, future, budget):
        """
        :type present: List[int]
        :type future: List[int]
        :type budget: int
        :rtype: int
        """
        dp = [0] * (budget + 1) 
        n = len(present)
        for i in range(n):
            cost = present[i]
            profit = future[i] - present[i]

            if profit <= 0:
                continue 

            for i in range(budget, cost - 1, -1):
                dp[i] = max(dp[i], dp[i-cost] + profit)
        return dp[budget]