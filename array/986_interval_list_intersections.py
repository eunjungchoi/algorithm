# Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that is either empty,
# or can be represented as a closed interval.
# For example, the intersection of [1, 3] and [2, 4] is [2, 3].)
#
#
#
# Example 1:

# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
# Note:
# 0 <= A.length < 1000
# 0 <= B.length < 1000
# 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
from typing import List


class Solution:
    """
    두 개의 닫힌 인터벌 리스트가 주어진다. 각 인터벌 리스트는 쌍으로 구분되고 정렬된 순서로 배열된다.
    이 두 인터벌 목록의 교차구간을 반환하라.
    """
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # two pointers

        if not A or not B:
            return []

        result = []
        i = j = 0

        while i < len(A) and j < len(B):
            late_start = max(A[i][0], B[j][0])   # start 값이 더 큰 값
            early_end = min(A[i][1], B[j][1])  # end 값이 더 작은 값

            if late_start <= early_end:
                result.append([late_start, early_end])

            # remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result

    def intervalIntersection2(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not B:
            return []

        result = []

        array = sorted(A + B, key=lambda x: x[0])
        start = array[0]

        for time in array[1:]:
            if start[0] <= time[0] <= start[1]:
                # 이제 끝나는 시간을 비교
                if start[1] <= time[1]:  # 앞 스케줄이 더 빨리 끝나면
                    result.append((time[0], start[1]))
                    # start = (start[1], time[1])
                    start = time
                elif time[1] < start[1]:
                    result.append((time[0], time[1]))
                    # start = (time[1], start[1])
            else:
                start = time

        return result


# 86 / 86 test cases passed.
# Status: Accepted
# Runtime: 132 ms
# Memory Usage: 14.8 MB
#
# Your runtime beats 100.00 % of python3 submissions.
# Your memory usage beats 12.52 % of python3 submissions.
