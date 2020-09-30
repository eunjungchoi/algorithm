# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution:
    """
    문자열로 표시된 두 개의 음이 아닌 정수 num1과 num2를 지정하면 num1과 num2의 합을 반환한다.

    참고:
    숫자1과 숫자2의 길이는 모두 < 5100이다.
    num1과 num2 모두 0-9 자리만 포함한다.
    num1과 num2 모두 선행 0을 포함하지 않는다.
    내장된 BigInteger 라이브러리를 사용하거나 직접 정수로 변환하지 마십시오.
    """

    def addStrings(self, num1: str, num2: str) -> str:
        # 전 가산기를 만드는 문제
        # 맨 뒷자리부터 carry 계산

        array = []
        i: int = len(num1) - 1
        j: int = len(num2) - 1
        carry: int = 0

        while i >= 0 or j >= 0:
            x1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            x2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            carry, sum_ = divmod(x1 + x2 + carry, 10)
            array.append(sum_)
            i -= 1
            j -= 1

        if carry:
            array.append(carry)

        return ''.join(map(str, array[::-1]))


# 315 / 315 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 14.4 MB
#
# Your runtime beats 78.47 % of python3 submissions.



