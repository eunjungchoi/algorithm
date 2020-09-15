# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#
# Constraints:
#
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 글자수 통일: 짧은 숫자 앞에 0 채우기
        diff = len(a) - len(b)
        if diff > 0:
            b = '0' * diff + b
        elif diff < 0:
            a = '0' * -diff + a

        result = ''
        i = len(a) - 1
        carry = 0

        while i >= 0:
            s = int(a[i]) + int(b[i]) + carry

            if s == 2:
                carry = 1
                result = '0' + result
            elif s == 3:
                carry = 1
                result = '1' + result
            else:
                result = str(s) + result
                carry = 0
            i -= 1

        if carry:
            result = str(carry) + result
        return result


# 294 / 294 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 14 MB
#
# Your runtime beats 66.15 % of python3 submissions.
# Your memory usage beats 22.46 % of python3 submissions.
