# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime?
# You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):  # 0부터 len(nums)까지 순회하며
            index = abs(nums[i]) - 1  # 인덱스가 가르키는 숫자를 다시 진짜 인덱스로 설정.
            nums[index] = - abs(nums[index])  # 그 인덱스의 값을 음수로 바꿔줌. 7은 -7로, -7은 -7로
        # 값이 양수인 인덱스를 찾으면 됨.
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 488 ms
# Memory Usage: 21.7 MB
#
# Your runtime beats 25.04 % of python3 submissions.
# Your memory usage beats 44.38 % of python3 submissions.
