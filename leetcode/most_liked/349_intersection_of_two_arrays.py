# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.

# 두 배열의 교집합을 구하라.
# 한쪽은 순서대로 탐색하고 다른 쪽은 정렬해서 이진 검색으로 값을 찾으면 검색 효율을 획기적으로 높일 수 있다.
# 시간 복잡도 O(n log n)

from bisect import bisect
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()  # 두번째 집합 정렬
        results = set()

        for n1 in nums1:
            index = bisect.bisect_left(nums2, n1)  # 이진 검색으로 일치 여부 판별
            if len(nums2) > 0 and index < len(nums2) and n1 == nums2[index]:
                results.add(n1)

        return results


# 60 / 60 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 86.05 % of python3 submissions.
# Your memory usage beats 90.42 % of python3 submissions.

