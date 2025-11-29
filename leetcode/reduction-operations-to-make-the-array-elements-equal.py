class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        numOfOps = 0
        res = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                numOfOps +=1

            res += numOfOps



        return res