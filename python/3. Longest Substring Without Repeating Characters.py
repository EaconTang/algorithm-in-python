# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        asc_list = []
        last_appear = [-1]*256
        max_length = 0
        left = 0
        last_no_repeat = -1
        length_list = []
        for i, char in enumerate(s):
            char_ascii = ord(char)
            global _length
            if last_appear[char_ascii] == -1:
                last_appear[char_ascii] = i
                _length = i - left + 1
            else:
                left = last_appear[char_ascii] + 1
                length_list.append(_length)
                last_appear[char_ascii] = i

        length_list.sort()
        return length_list

        # violient solution
        # gen = lambda l:(_ for _ in l)
        # max_length = 0
        # for i, char in gen(enumerate(s)):
        #     substring = []
        #     for _char in gen(s[i:]):
        #         if _char not in substring:
        #             substring.append(_char)
        #             # print substring, " length:", len(substring)
        #             substring_len = len(substring)
        #             if substring_len > max_length:
        #                 max_length = substring_len
        #         else:
        #             substring_len = len(substring)
        #             if substring_len > max_length:
        #                 max_length = substring_len
        #             # print "\tlength: ", max_length
        #             # print "\tsubstring: ", substring
        #             substring = [_char]

        return max_length


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring("abc")
    # print Solution().lengthOfLongestSubstring(test)