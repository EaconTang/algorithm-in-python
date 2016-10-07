# -*- coding: utf-8 -*-
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

Subscribe to see which companies asked this question
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        s = s.lower()
        i = start = 0
        j = end = len(s) - 1
        while 1:
            if i > j: break
            while not s[i].isalnum() and not s[i].isalpha():
                if i == end: return True
                i += 1
            while not s[j].isalnum() and not s[j].isalpha():
                # if j == start: return True
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    print Solution().isPalindrome("123```abcd`CB``A3 21")
    print Solution().isPalindrome(" ")
    print Solution().isPalindrome(".,")
