class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        
        # 'stack' stores indices of days that haven't found a warmer day yet.
        # This stack will maintain indices such that temperatures are in decreasing order.
        stack = [] 
        
        for curr_day, curr_temp in enumerate(temperatures):
            # While the stack is not empty and the current temperature is warmer
            # than the temperature of the day at the top of the stack...
            while stack and curr_temp > temperatures[stack[-1]]:
                # We found a warmer day for 'prev_day'
                prev_day = stack.pop()
                
                # The wait time is the difference in indices
                res[prev_day] = curr_day - prev_day
            
            # Add the current day to the stack to be resolved later
            stack.append(curr_day)
            
        return res