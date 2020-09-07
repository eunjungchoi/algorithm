# # 겹치는 구간을 병합하라
#
# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019.
# Please reset to default code definition to get new method signature.
#
#
# Constraints:
# intervals[i][0] <= intervals[i][1]

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []

        for item in sorted(intervals, key=lambda x: x[0]):
            if merged and item[0] <= merged[-1][1]:
                merged[-1][1] = max(item[1], merged[-1][1])
            else:
                merged += [item]

        return merged


# 169 / 169 test cases passed.
# Status: Accepted
# Runtime: 80 ms
# Memory Usage: 15.7 MB
#
# Your runtime beats 98.49 % of python3 submissions.
# Your memory usage beats 30.40 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
