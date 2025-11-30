class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        for n , c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if k == len(res):
                    return res
#         # find frequency
#         freq = Counter(nums)
#         # construct heap
#         heap = []
#         for num in freq.keys():
#             heappush(heap, (freq[num], num))
#             if len(heap) > k:
#                 heappop(heap)
#         # return items in heap
#         return [item[1] for item in heap]

# # freq size: O(m)
# # size heap: O(k)