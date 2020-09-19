# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:
#
# You can assume that you can always reach the last index.
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        times = 1
        left = 0
        right = nums[0]

        while right < len(nums) - 1:
            nxt = max(i + nums[i] for i in range(left, right + 1))
            # left와 right 사이에 있는 후보군 중에 최대한 멀리 갈 수 있는 인덱스
            left, right = right + 1, nxt
            times += 1
        return times


# 92 / 92 test cases passed.
# Status: Accepted
# Runtime: 100 ms
# Memory Usage: 16 MB
#
# Your runtime beats 72.05 % of python3 submissions.
# Your memory usage beats 57.77 % of python3 submissions.

