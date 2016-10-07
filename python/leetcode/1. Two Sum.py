# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        Time: O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indice_num_dict = {}
        for id,num in enumerate(nums):
            indice_num_dict[num] = id
        for i, num_i in enumerate(nums):
            if (target - num_i) in nums:
                j = indice_num_dict.get(target - num_i)
                if j != i:
                    return [i, j]
        return []


if __name__ == '__main__':
    import time
    s = time.time()
    print Solution().twoSum([3,2,4], 6)
    print time.time() - s