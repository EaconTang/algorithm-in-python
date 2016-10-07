# -*- coding: utf-8 -*-
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


if __name__ == '__main__':
    print Solution().climbStairs(10)