# Given a non negative integer number num.
# For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation
# and return them as an array.
#
# Example 1:
#
# Input: 2
# Output: [0,1,1]
# Example 2:
#
# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)).
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss?
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        # return [bin(i).count('1') for i in range(num + 1)]

        # (i & (i -1)) is actually Brian Kernighan’s Algorithm, so always keep it handy for counting ones
        # 브라이언 커니핸 알고리즘 + 메모이제이션 활용
        memo = [0] * (num + 1)

        for i in range(1, num + 1):
            memo[i] = memo[(i & (i - 1))] + 1

        return memo


# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 104 ms
# Memory Usage: 20.8 MB
#
# Your runtime beats 49.35 % of python3 submissions.
# Your memory usage beats 19.48 % of python3 submissions.
