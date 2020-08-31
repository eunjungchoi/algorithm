# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer,
# the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
import math


class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        left = 1
        right = x

        if x < 2:
            return x

        while left < right:
            mid = left + math.floor((right - left) / 2)

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid + 1

        return left - 1


# 1017 / 1017 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 74.71 % of python3 submissions.
# Your memory usage beats 25.35 % of python3 submissions.
