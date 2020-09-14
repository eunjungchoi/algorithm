# Given an array nums of n integers where n > 1,  return an array output
# such that output[i] is equal to the product of all the elements of nums except nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements
# of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity?
# (The output array does not count as extra space for the purpose of space complexity analysis.)

# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

# 왼쪽 곱셈 결과에 오른쪽 값을 차례로 곱셈
# 왼쪽부터 곱해서 result에 추가한다.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 곱셈 결과는 그대로 out 리스트 변수에 담기게 되며, 마지막 값 곱셈을 제외하여 결과는 [1, 1, 2, 6]이 된다.
        out = []
        p = 1

        # 왼쪽 곱셈. 변수 i가 오른쪽으로 이동하면서 다음 인덱스로 넘기기 전에 p에 현재 값을 곱해줌.
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        # 오른쪽에서 부터 곱해줌.
        for i in range(len(nums) - 1, 0 - 1, -1):  # 마지막 인덱스부터 시작해서 역으로 -1씩 줄어드는 형태.
            out[i] = out[i] * p
            p = p * nums[i]

        return out


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 116 ms
# Memory Usage: 20.5 MB
#
# Your runtime beats 96.38 % of python3 submissions.
# Your memory usage beats 63.30 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
