#
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:
#
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note: 1 <= N <= 10 ^ 9.


class Solution:
    """
    양의 정수 N을 주어질 때, 연속적인 양의 정수의 합으로 쓸 수 있는 방법은 몇 가지인가?

    """
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        N can be expressed as k, k + 1, k + 2, ..., k + (i - 1), where k is a positive integer; therefore
        N = k * i + (i - 1) * i / 2 => N - (i - 1) * i / 2 = k * i,
        which implies that as long as N - (i - 1) * i / 2 is k times of i,
        we get a solution corresponding to i;
        Hence iteration of all possible values of i, starting from 1, will cover all cases of the problem.
        """
        result = 0
        i = 1
        while N > i * (i - 1) // 2:
            if (N - i * (i - 1) // 2) % i == 0:
                result += 1
            i += 1
        return result


# 170 / 170 test cases passed.
# Status: Accepted
# Runtime: 212 ms
# Memory Usage: 14 MB
#
# Your runtime beats 47.41 % of python3 submissions.
# Your memory usage beats 13.07 % of python3 submissions.
