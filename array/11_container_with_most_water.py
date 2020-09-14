# Given n non-negative integers a1, a2, ..., an ,
# where each represents a point at coordinate (i, ai). n vertical lines are drawn
# such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
#
#
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer로 풀기
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# 50 / 50 test cases passed.
# Status: Accepted
# Runtime: 164 ms
# Memory Usage: 15.5 MB
#
# Your runtime beats 29.53 % of python3 submissions.
# Your memory usage beats 21.16 % of python3 submissions.
