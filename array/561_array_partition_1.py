# Given an array of 2n integers,
# your task is to group these integers into n pairs of integer,
# say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
#
# Example 1:
# Input: [1,4,3,2]
#
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
# Note:
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].

# n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
# 페어의 min()을 합산했을 때 최대를 만드는 것은 결국 min()이 되도록 커야 한다는 듯이다.
# 정렬된 상태에서 앞에서부터 오름차순으로 페어를 만들면, 항상 최대 min() 페어를 유지할 수 있다.
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 1. 오름차순 풀이
        #         sum_ = 0
        #         pair = []
        #         nums.sort()

        #         for n in nums:
        #             pair.append(n)
        #             if len(pair) == 2:
        #                 sum_ += min(pair)
        #                 pair = []
        #         return sum_

        # 2. 짝수번째 값 계산
        # 정렬된 상태에서는 짝수 번째에 항상 작은 값이 위치함 (0부터 시작하기 때문에)
        # sum_ = 0
        # nums.sort()

        # for i, n in enumerate(nums):
        #     if i % 2 == 0:
        #         sum_ += n
        # return sum_

        # 3. pythonic way
        return sum(sorted(nums)[::2])


# 81 / 81 test cases passed.
# Status: Accepted
# Runtime: 264 ms
# Memory Usage: 16.2 MB
#
# Your runtime beats 99.75 % of python3 submissions.
# Your memory usage beats 85.28 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
