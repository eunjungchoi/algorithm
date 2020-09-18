# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#
#
# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10

class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
       

        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans