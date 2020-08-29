# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left, right = 0, len(height) - 1
        left_max = height[left]
        right_max = height[right]

        volume = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume


# 315 / 315 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 14.3 MB
#
# Your runtime beats 92.54 % of python3 submissions.
# Your memory usage beats 96.23 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
