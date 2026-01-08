class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 'curr' tracks the number of currently open parentheses
        curr = 0
        # 'res' stores the maximum value 'curr' ever reaches
        res = 0
        
        # Iterate through each character 'c' in the input string 's'
        for c in s:
            # If we encounter an opening bracket, we go deeper
            if c == '(':
                curr += 1
                # Update the result immediately to capture peak depth
                if curr > res:
                    res = curr
            # If we encounter a closing bracket, we come back up
            elif c == ')':
                curr -= 1
        
        # Return the deepest level reached
        return res