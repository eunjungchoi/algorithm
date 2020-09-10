# Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
#
#
#
# Example 1:
#
# Input: 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
# Example 2:
#
# Input: 00000000000000000000000010000000
# Output: 1
# Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
# Example 3:
#
# Input: 11111111111111111111111111111101
# Output: 31
# Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
#
#
# Note:
#
# Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
#
#
# Follow up:
#
# If this function is called many times, how would you optimize it?

# 부호 없는 정수형 (unsigned integer) 을 입력받아 1비트의 개수를 출력하라.

# 이 문제의 결과는 모두 0으로 구성된 비트들과의 해밍 거리로, 이를 해밍 가중치 hamming weight 라고 부른다.
# 이 문제의 답은 해밍 가중치의 값이라고 할 수 있다.
# 해밍거리는 A XOR B 이다. B가 0일 때 XOR는 생략 가능하다.



class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1. 해밍 거리 계산하기
        # return bin(n ^ 0).count('1')
        # return bin(n).count('1')

        # 2. 비트 연산
        # 1을 뺀 값과 AND 연산을 할 때마다 비트가 1씩 빠지게 된다.
        # 0이 될 때까지 이 작업을 반복하면 전체 비트에서 1의 개수가 몇 개인지 알 수 있다는 얘기다.
        # 파이썬 뿐 아니라 모든 언어에서 동일하게 활용가능하다. (좀더 범용적인 알고리즘)
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1

        return count


# 601 / 601 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 95.66 % of python3 submissions.
# Your memory usage beats 50.64 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고
