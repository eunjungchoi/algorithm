# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#

# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#
#
# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10

# 히스토그램에서 가장 큰 직사각형의 면적을 찾아라.

from typing import List


class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        # 앞 그래프보다 뒤의 그래프가 작을 때 뒤의 그래프가 right boundary가 되고, 앞앞 그래프가 left boundary가 되는 구조.
        # stack에 높이 오름차순으로  인덱스를 쌓아나가다가  더 낮은 높이가 나오면  stack에서 pop해서 면적 계산.

        height.append(0)  # 0을 추가해서 가장 오른쪽 ending point 이자 right boundary를 설정.
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:  # 현재 인덱스의 높이가  stack에 저장된 top 인덱스의 높이보다 작으면,
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                # i : 오른쪽 바운더리 (면적에 포함x), stack[-1]: 왼쪽 바운더리 (면적에 포함 x).  -1을 해줘야 그 사이에 있는 공간만 계산.
                ans = max(ans, h * w)

            # 현재 인덱스의 높이보다 큰 값들을 stack에서 다 제거해 준 다음에   현재 인덱스를 stack에 삽입.
            stack.append(i)

        height.pop()

        return ans


# 96 / 96 test cases passed.
# Status: Accepted
# Runtime: 104 ms
# Memory Usage: 15.6 MB
#
# Your runtime beats 90.13 % of python3 submissions.
# Your memory usage beats 90.70 % of python3 submissions.
