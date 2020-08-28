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

        for i, item in enumerate(nums):
            if item in candidates:
                return [candidates[item], i]

            candidates[target - item] = i

        return []


# after fix:
# 29 / 29 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 15.1 MB

# Your runtime beats 95.83 % of python3 submissions.
# Your memory usage beats 58.46 % of python3 submissions.

