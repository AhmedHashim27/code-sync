class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n = len(arr)
        if n < 3:
            return 0

        longest = 0
        i = 1 

        while i < len(arr) - 1:
            peak = arr[i-1] < arr[i] and arr[i+1] < arr[i]

            if peak:
                l = i - 1
                while l > 0 and arr[l-1] < arr[l]:
                    l -=1

                r = i + 1
                while r < len(arr) -1 and arr[r] > arr[r+1]:
                    r +=1

                currLen = (r -l + 1)
                longest = max(longest, currLen)

                i = r
            else:
                i += 1
        return longest