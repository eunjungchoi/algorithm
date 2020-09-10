# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4


# 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.
# 딱 1개의 엘리먼트를 찾는데 적당한 연산자:  XOR

# 두 번 등장한 엘리먼트는 0으로 초기화되고,  한번만 ㅏ등장하는 엘리먼트는 그 값을 온전히 보존한다.  (그 값을 더해준다)
# 배열의 모든 값을 XOR 하면 단 한 번만 등장하는 엘리먼트만 그 값이 남게 된다.

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num

        return result


# 16 / 16 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Memory Usage: 16.3 MB
#
# Your runtime beats 89.98 % of python3 submissions.
# Your memory usage beats 58.97 % of python3 submissions.
