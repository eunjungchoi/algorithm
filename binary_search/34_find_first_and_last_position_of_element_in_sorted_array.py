# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
#
# Constraints:
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non decreasing array.
# -10^9 <= target <= 10^9
from typing import List


class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def get_extreme_index(self, nums: List[int], target: int, left: bool = True):
        low = 0
        high = len(nums)

        while low < high:
            mid = low + (high - low) // 2

            if target < nums[mid] or (left and target == nums[mid]):  # # mid 기준으로 왼쪽을 서치
                high = mid
            else:  # nums[mid] < target  # mid 기준으로 오른쪽을 서치.  mid가 new left가 됨
                low = mid + 1

        return low

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = self.get_extreme_index(nums, target, True)
        if left_index == len(nums) or nums[left_index] != target:
            return [-1, -1]

        return [left_index, self.get_extreme_index(nums, target, False) - 1]


# 88 / 88 test cases passed.
# Status: Accepted
# Runtime: 76 ms
# Memory Usage: 15.2 MB
#
# Your runtime beats 99.32 % of python3 submissions.
# Your memory usage beats 25.83 % of python3 submissions.
