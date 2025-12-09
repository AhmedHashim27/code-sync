class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        curr = ""
        num = 0

        for char in s:
            if char.isdigit():
                num = (num * 10) + int(char)

            elif char == "[":
                stack.append((curr, num))
                curr = ""
                num = 0
            elif char == "]":

                prev, n = stack.pop()
                curr = prev + (n * curr)
            else:
                curr += char
        return curr