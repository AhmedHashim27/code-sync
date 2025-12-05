class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        stack = []

        def dfs(openN, close):
            if openN == close == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                dfs(openN + 1, close)
                stack.pop()

            if openN > close:
                stack.append(")")
                dfs(openN, close + 1)
                stack.pop()
        dfs(0,0)
        return res