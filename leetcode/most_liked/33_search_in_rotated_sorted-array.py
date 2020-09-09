# You are given an integer array nums sorted in ascending order, and an integer target.
#
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# If target is found in the array return its index, otherwise, return -1.
#
#
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4

# 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라
# 피벗을 기준으로 한 이진 검색 

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

            # 최솟값을 찾아 피벗 설정
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # 피벗 기준 이진 검색
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1


# 195 / 195 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 79.70 % of python3 submissions.
# Your memory usage beats 89.35 % of python3 submissions.
