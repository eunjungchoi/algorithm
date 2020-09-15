# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        result = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if not result else result[-1] - result[0] + 1


# 307 / 307 test cases passed.
# Status: Accepted
# Runtime: 216 ms
# Memory Usage: 15 MB
#
# Your runtime beats 74.34 % of python3 submissions.
# Your memory usage beats 63.87 % of python3 submissions.
