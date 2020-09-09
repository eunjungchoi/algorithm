# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
# Input: [10,2]
# Output: "210"
# Example 2:
#
# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.
from typing import List


class Solution:
    @staticmethod
    def to_swap(n1: int, n2: int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:
        # 삽입 정렬 구현
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                j -= 1
            i += 1

        return str(int(''.join(map(str, nums))))
