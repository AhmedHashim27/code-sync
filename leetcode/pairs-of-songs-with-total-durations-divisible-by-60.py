class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainders = [0] * 60
        
        count = 0
        
        for t in time:
            # 1. Calculate the remainder of the current song duration
            r = t % 60
            
            # 2. Determine the 'target' remainder needed to form a sum divisible by 60.
            # Usually, if we have remainder r, we need (60 - r).
            # Example: If r=20, we need 40. (20+40)%60 == 0.
            # Edge Case: If r=0, we need 0. (60 - 0) is 60, and 60 % 60 is 0.
            target = (60 - r) % 60
            
            # 3. Add the number of times we've seen the 'target' remainder so far.
            # These are valid pairs (previous_song, current_song).
            count += remainders[target]
            
            # 4. Record the current song's remainder for future pairs.
            remainders[r] += 1
            
        return count