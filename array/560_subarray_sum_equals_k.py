# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2
#
#
# Constraints:
#
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
import collections
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = collections.Counter()
        count[0] = 1

        total = 0
        result = 0
        # [1, 2, 3, 4, 5]   k = 7
        for num in nums:
            total += num
            result += count[
                total - k]  # currSum - target = oldSum  (oldSum이 카운트에 있다면,  oldSum을 이루는 배열들 바로 다음에 오는 배열의 합이  k가 됨. )
            count[total] += 1

        return result


# 81 / 81 test cases passed.
# Status: Accepted
# Runtime: 136 ms
# Memory Usage: 16.1 MB
#
# Your runtime beats 89.39 % of python3 submissions.
# Your memory usage beats 79.09 % of python3 submissions.
