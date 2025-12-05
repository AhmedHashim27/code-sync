class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []

        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        res = []
        part = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(part))
                return 

            letters = phone_map[digits[i]]

            for char in letters:
                part.append(char)
                dfs(i+1)
                part.pop()

        dfs(0)
        return res