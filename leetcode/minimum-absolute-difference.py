class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        arr.sort()
        
        min_diff = float('inf')
        res = []
        
        # Step 2: Single pass to find min_diff and collect pairs
        # We iterate up to the second to last element
        for i in range(len(arr) - 1):
            
            # Calculate difference between neighbor elements
            # Since array is sorted, arr[i+1] is always >= arr[i]
            diff = arr[i + 1] - arr[i]
            
            # Case 1: Found a new minimum difference
            if diff < min_diff:
                min_diff = diff
                # Reset result list with this new pair
                res = [[arr[i], arr[i + 1]]]
            
            # Case 2: Found a difference equal to current minimum
            elif diff == min_diff:
                # Append this pair to the existing list
                res.append([arr[i], arr[i + 1]])
                
            # Case 3 (Implicit): diff > min_diff -> Do nothing
            
        return res