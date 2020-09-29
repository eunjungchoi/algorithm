# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible,
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        다음에 올 순열을 구현하라.
        이 순열은 사전통계학적으로 숫자의 순열보다 큰 순열로 번호를 재배열한다. 
        그러한 배열이 불가능할 경우, 가능한 가장 낮은 순서(즉, 오름차순으로 정렬)로 재배열해야 한다.
        교체품은 제자리에 있어야 하며 일정한 여분의 메모리만 사용해야 한다.
        """

        i = j = len(nums) - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # nums[i-1] < nums[i]
        if i == 0:  # nums are in descending order
            nums.reverse()
            return

        k = i - 1  # find the last "ascending" position

        while nums[j] <= nums[k]:
            j -= 1
        # j: 맨 마지막 인덱스에서 왼쪽으로 출발해서 처음으로 i-1의 값보다 큰 값일 때의 수의 인덱스.
        nums[k], nums[j] = nums[j], nums[k]

        left, right = i, len(nums) - 1  # reverse the second part

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# 265 / 265 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14.2 MB
#
# Your runtime beats 93.09 % of python3 submissions.
