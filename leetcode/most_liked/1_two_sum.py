# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = {}
        result = []

        for i, item in enumerate(nums):
            if item in candidates:
                result.append(candidates[item])
                result.append(i)
            else:
                candidates[target - item] = i

        return result

# Your runtime beats 76.34 % of python3 submissions.
