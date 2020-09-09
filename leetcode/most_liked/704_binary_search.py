# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
#
#
# Example 1:
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
# Example 2:
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
# Note:
#
# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].
from bisect import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #         # iterative
        #         left = 0
        #         right = len(nums) - 1

        #         while left <= right:
        #             mid = (left + right) // 2

        #             if target < nums[mid]:
        #                 right = mid - 1
        #             elif nums[mid] < target:
        #                 left = mid + 1
        #             else:
        #                 return mid

        #         return -1

        # 이진 검색 모듈
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        return -1


# 46 / 46 test cases passed.
# Status: Accepted
# Runtime: 256 ms
# Memory Usage: 15 MB
#
# Your runtime beats 82.41 % of python3 submissions.
# Your memory usage beats 53.21 % of python3 submissions.

