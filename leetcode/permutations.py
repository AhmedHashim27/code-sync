class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        res = []
        def backtrack(first):
            n = len(nums)

            if first == n:
                res.append(nums[:])
                return

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first] # Place i-th number at 'first'
                
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first] # Undo
        backtrack(0)
        return res
        # permutaion = [[]]
        # for n in nums:
        #     new_perm = []
        #     for perm in permutaion:
        #         for i in range(len(perm) + 1):
        #             perm_copy = perm[:]
        #             perm_copy.insert(i, n)
        #             new_perm.append(perm_copy)
        #     permutaion = new_perm
        # return permutaion







        # permutations = [[]]
        # for n in nums:
        #     new_perms = []
        #     for perm in permutations:
        #         for i in range(len(perm) + 1):
        #             perm_copy = perm[:]
        #             perm_copy.insert(i, n)
        #             new_perms.append(perm_copy)
        #     permutations = new_perms
        # return permutations