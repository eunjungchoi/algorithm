# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#
#
# Example 1:
#
#
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:
#
# Input: matrix = []
# Output: 0
# Example 3:
#
# Input: matrix = [["0"]]
# Output: 0
# Example 4:
#
# Input: matrix = [["1"]]
# Output: 1
# Example 5:
#
# Input: matrix = [["0","0"]]
# Output: 0

# 가장 큰 직사각형의 면적을 구하라.

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # dynamic programming and stack

        # 예외 처리
        if not matrix or not matrix[0]:
            return 0

        # 자료 구조
        heights = [0] * (len(matrix[0]) + 1)
        result = 0

        # 순회

        for row in matrix:

            for col in range(len(matrix[0])):
                # height update
                heights[col] = heights[col] + 1 if row[col] == '1' else 0

            stack = [-1]

            for col in range(len(matrix[0]) + 1):
                while heights[col] < heights[stack[-1]]:    # height[i] 보다 height[i-1]이 작을 때 앞의 직사각형 사이즈를 계산
                    h = heights[stack.pop()]
                    w = col - stack[-1] - 1
                    result = max(result, h * w)

                stack.append(col)

        return result


# 66 / 66 test cases passed.
# Status: Accepted
# Runtime: 180 ms
# Memory Usage: 14.6 MB
#
# Your runtime beats 99.72 % of python3 submissions.
# Your memory usage beats 24.94 % of python3 submissions.
