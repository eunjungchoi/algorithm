# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
from typing import List


class Solution:
    @staticmethod
    def max_subarray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        curr_sum, max_sum = 0, 0
        for num in nums:
            curr_sum = max(0, curr_sum + num)
            max_sum = max(curr_sum, max_sum)
        return max_sum
