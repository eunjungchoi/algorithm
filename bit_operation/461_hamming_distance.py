# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

# 두 정수를 입력받아 몇 비트가 다른지 계산하라.
#
# 자연어 처리에서도 널리 쓰이는 해밍 거리는 두 정수 또는 두 문자열의 차이를 말한다.
# 예를 들면 karolin과 kathlin의 차이는 3이고 1011101과 1001001의 차이는 2다.
# 문자열의 경우 해밍 거리는 다른 자리의 문자 개수가 되며, 이진수의 경우 다른 위치의 비트 개수가 된다.


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # x^y XOR 결과는 정수가 나오므로 이를 bin() 을 이용해 이진수로 변경하고,
        # 여기서 1의 전체 개수를 헤아리면 다른 자리의 개수, 즉 해밍 거리 값이 나온다.
        return bin(x ^ y).count('1')


# 149 / 149 test cases passed.
# Status: Accepted
# Runtime: 20 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 98.93 % of python3 submissions.
# Your memory usage beats 61.86 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.


