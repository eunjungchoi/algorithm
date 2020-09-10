# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
#
# Note:
#
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
#
# Example 1:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# Example 2:
#
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Example 3:
#
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#
#
# Constraints:
#
# 2 <= nums.length <= 3 * 104
# -1000 <= nums[i] <= 1000
# nums is sorted in increasing order.
# -1000 <= target <= 1000

# 두 수의 합 2
# 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.


from bisect import bisect
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # binery search
        #         for k, v in enumerate(numbers):
        #             left = k+1
        #             right = len(numbers) -1

        #             expected = target - v

        #             while left <= right:
        #                 mid = left + (right - left) // 2
        #                 if numbers[mid] < expected:
        #                     left = mid + 1
        #                 elif expected < numbers[mid]:
        #                     right = mid - 1
        #                 else:
        #                     return k+1, mid+1

        # using bisect
        # for k, v in enumerate(numbers):
        #     expected = target - v
        #     i = bisect.bisect_left(numbers, expected, lo=k + 1)
        #     if i < len(numbers) and numbers[i] == expected:
        #         return [k + 1, i + 1]

        # two pointers
        left, right = 0, len(numbers) - 1

        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]


# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 68 ms
# Memory Usage: 14.4 MB
#
# bisect
# Your runtime beats 62.26 % of python3 submissions.
# Your memory usage beats 40.28 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.

# two pointer
# Your runtime beats 62.26 % of python3 submissions.
# Your memory usage beats 98.44 % of python3 submissions.


