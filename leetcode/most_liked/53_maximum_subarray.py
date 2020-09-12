# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# 합이 최대가 되는 연속 서브 배열을 찾아 합을 리턴하라.
# 메모이제이션을 이용

from typing import List


class Solution:
    @staticmethod
    def max_subarray(self, nums: List[int]) -> int:
        # 1. 메모이제이션
        sums: List[int] = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i - 1] if sums[i - 1] > 0 else 0))

        return max(sums)

        # 2. 카데인 알고리즘
        # 1977년에 제안된 매우 유명한 컴퓨터 과학 알고리즘. 제인 카데인이 O(n)에 풀이가 가능하도록 고안.
        # 각 단계마다 최댓값을 담아 어디서 끝나는지를 찾는 문제. O(n)
        # if max(nums) < 0:
        #     return max(nums)
        #
        # curr_sum, max_sum = 0, 0
        # for num in nums:
        #     curr_sum = max(0, curr_sum + num)
        #     max_sum = max(curr_sum, max_sum)
        # return max_sum


# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 64 ms
# Memory Usage: 14.6 MB
#
# Your runtime beats 89.17 % of python3 submissions.
# Your memory usage beats 49.11 % of python3 submissions.
