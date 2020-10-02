# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# Follow up: The overall run time complexity should be O(log (m+n)).
#
#
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# Example 3:
#
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# Example 4:
#
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# Example 5:
#
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
from typing import List


class Solution:
    """
    각각 크기가 m과 n인 정렬된 배열 두 개가 주어진다.
    정렬된 배열 두 개의 중위수를 반환하라.

    후속 조치: 전체 실행 시간 복잡도는 O(log(m+n))이어야 한다.
    """

    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        total = []
        key1 = 0 if len(nums1) else None
        key2 = 0 if len(nums2) else None

        count: int = ((len(nums1) + len(nums2)) // 2) + 1
        while count > 0 and (key1 is not None or key2 is not None):
            append_1 = False
            append_2 = False

            if key1 is None:
                append_2 = True
            elif key2 is None:
                append_1 = True
            else:
                if nums1[key1] < nums2[key2]:
                    append_1 = True
                else:
                    append_2 = True

            if append_1:
                total.append(nums1[key1])
                if key1 < len(nums1) - 1:
                    key1 += 1
                else:
                    key1 = None
            elif append_2:
                total.append(nums2[key2])
                if key2 < len(nums2) - 1:
                    key2 += 1
                else:
                    key2 = None

            count -= 1

        if (len(nums1) + len(nums2)) % 2 == 1:
            return total[-1]
        else:
            return (total[-2] + total[-1]) / 2


# 2091 / 2091 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Memory Usage: 14.5 MB
#
# Your runtime beats 83.95 % of python3 submissions.
# Your memory usage beats 71.04 % of python3 submissions.
