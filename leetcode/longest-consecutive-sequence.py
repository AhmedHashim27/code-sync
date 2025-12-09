class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



        numsSet = set(nums)
        streak = 0
        for n in numsSet:
            if (n-1) not in numsSet:
                lenght = 0
                while (n + lenght) in numsSet:
                    lenght +=1
                streak = max(streak, lenght)
        return streak

        # length = set()
        # for num in nums:
        #     length.add(num)
        # max_length = 0
        # unique_nums = list(length)
        # for num in unique_nums:
        #     if num + 1 not in length:
        #         total_length = 1
        #         prev_num = num - 1	
        #         while prev_num in length:
        #             total_length += 1
        #             prev_num -= 1
        #         max_length = max(max_length, total_length)
        # return max_length