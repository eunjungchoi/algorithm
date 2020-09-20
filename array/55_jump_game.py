# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what.
# Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i][j] <= 10^5
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 0. 현재까지 최대로 멀리 갈 수 있는 인덱스와 현재 인덱스를 비교.
        # max_position = 0
        # for i, num in enumerate(nums):
        #     if i > max_position:  # 누적으로 가장 멀리 갈 수 있는 인덱스가  현재 인덱스보다 작으면  끝까지 못 간다는 것.
        #         return False
        #     max_position = max(max_position, i + num)  # 최대로 멀리 갈 수 있는 인덱스를 업데이트.
        #
        # return True

        # 1. 처음부터 시작해서  가장 멀리 갈 수 있는 인덱스가 맨 마지막 인덱스보다 작으면 false
        #         left = 0
        #         right = nums[0]

        #         while left <= right and right < len(nums) - 1:
        #             max_ = max([i + nums[i] for i in range(left, right + 1)])
        #             left = right + 1
        #             right = max_

        #         if right < len(nums) -1:
        #             return False

        #         return True

        # 2.  뒤에서부터 앞으로 이동하며 last position 업데이트 
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i

        return last == 0


# 75 / 75 test cases passed.
# Status: Accepted
# Runtime: 88 ms
# Memory Usage: 15.8 MB
#
# Your runtime beats 85.57 % of python3 submissions.
# Your memory usage beats 66.85 % of python3 submissions.

