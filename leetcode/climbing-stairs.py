class Solution(object):
    def climbStairs(self, n):

        one , two = 1, 1
        for i in range( n -1):
            temp = one 
            one = one + two 
            two = temp
        return one
        # first_step = 1
        # second_step = 1
        # for i in range(2, n + 1):
        #     third_step = first_step + second_step
        #     first_step = second_step
        #     second_step = third_step
        # return second_step