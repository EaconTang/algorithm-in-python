# -*- coding: utf-8 -*-
"""
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.
For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        digit_sum = sum([int(_) for _ in str(num)])
        if digit_sum > 9:
            return self.addDigits(digit_sum)
        return digit_sum


if __name__ == '__main__':
    print Solution().addDigits(13)
    print Solution().addDigits(13289384)
    print Solution().addDigits(99)

