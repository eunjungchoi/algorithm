# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1

# Follow up:
#
# Your algorithm should run in O(n) time and uses constant extra space.
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #  Basic idea:
        # 1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        #     so we only have to care about those elements in this range and remove the rest.
        # 2. we can use the array index as the hash to restore the frequency of each number within
        #      the range [1,...,l+1]

        nums.append(0)
        length = len(nums)

        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= length:   # delete those useless elements
                nums[i] = 0

        for i in range(len(nums)):
            nums[nums[i] % length] += length   # use the index as the hash to record the frequency of each number

        for i in range(1, len(nums)):
            if nums[i] // length == 0:  # 값을 순회하며  값을 length로 나눈 몫이 0이면  그게 답
                return i

        return length


# 165 / 165 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 96.51 % of python3 submissions.
# Your memory usage beats 54.70 % of python3 submissions.
