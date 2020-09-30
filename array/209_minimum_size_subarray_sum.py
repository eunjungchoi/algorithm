# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.
#
# Example:
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
from typing import List


class Solution:
    """
    n개의 양의 정수 배열과 양의 정수 s가 주어진다. 연속 부분 배열의 합이 s와 같거나 크게 되는 최소 배열의 길이를 찾아라.
    만약 없다면, 대신 0을 반환하라.

    슬라이딩 윈도우 sliding window 
    """
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        left = 0
        length = len(nums)
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]

            while sum_ >= s:
                # A[left] ... A[i] 까지의 합이 s와 같거나 크다는 말.
                length = min(length, i - left + 1)
                sum_ -= nums[left]  # left 를 슬라이딩 윈도우에서 빼주기
                left += 1

        return length


# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 16.7 MB
#
# Your runtime beats 99.90 % of python3 submissions.
