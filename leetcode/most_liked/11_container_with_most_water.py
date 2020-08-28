
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        last = len(height) - 1
        for i, item in enumerate(height):
            key = i + 1
            while key <= last:
                h = height[i] if height[i] <= height[key] else height[key]
                w = key - i
                area = w * h
                if area > max_area:
                    max_area = area
                key += 1

        return max_area