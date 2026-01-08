class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_count = 0
        
        # 'current_count' tracks the current streak of 1s
        current_count = 0
        
        for num in nums:
            if num == 1:
                # Continue the streak
                current_count += 1
            else:
                # Streak broken by a 0.
                # Check if the streak we just finished is the largest so far.
                if current_count > max_count:
                    max_count = current_count
                # Reset counter for the next streak
                current_count = 0
                
        # CRITICAL STEP:
        # If the array ends with 1s, the else block above is never reached.
        # We must perform one final check.
        if current_count > max_count:
            max_count = current_count
            
        return max_count