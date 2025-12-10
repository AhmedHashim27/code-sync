class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        seq = []

        def find_greater_at_idx(num):
            start = 0
            end = len(seq) - 1
            while start <= end:
                mid = (start + end) // 2
                if seq[mid] >= num:
                    end = mid - 1
                else:
                    start = mid + 1
            return start

        for n in nums:
            if not seq or n > seq[-1]:
                seq.append(n)
            elif n == seq[-1]:
                continue
            else:
                greater_idx = find_greater_at_idx(n)
                seq[greater_idx] = n
        return len(seq)