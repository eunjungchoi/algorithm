# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = -2, b = 3
# Output: 1

# 두 정수 a와 b의 합을 구하라. + 또는 - 연산자는 사용할 수 없다.
# 비트 연산 만으로 풀이해야 하는 문제이다.
# 전가산기를 구현해본다.


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask는 비트 마스크로, 음수 처리를 위해 2의 보수로 만들어주는 역할을 함.
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF

        # 파이썬에서는 이진수로 변환하면 앞에 0b 식별자가 항상 붙음.  슬라이싱으로 이 부분을 떼냄
        # zfill(32)로 32비트 자릿수를 맞춰줌.
        a_bin = bin(a & MASK)[2:].zfill(32)
        b_bin = bin(b & MASK)[2:].zfill(32)

        result = []
        carry = 0
        sum_ = 0

        # 처리한 값을 뒷부분부터, 낮은 자릿수부터 하나씩 전가산기를 통과하면서 결과를 채워나가면 됨.
        for i in range(32):
            A = int(a_bin[31 - i])
            B = int(b_bin[31 - i])

            q1 = A & B
            q2 = A ^ B
            q3 = q2 & carry
            sum_ = carry ^ q2
            carry = q1 | q3

            result.append(str(sum_))

        # 마지막 반복이 끝난 후 아직 carry 값이 남아있다면 자릿수가 하나 더 올라간 것이므로 1을 추가.
        if carry == 1:
            result.append('1')

            # 초과 자릿수 처리
        # 이렇게 되면 최대 33비트가 되겠지만,  마지막 마스킹 작업을 통해 이 값을 날아가게 된다.
        # result는 낮은 자릿수부터 채웠으므로 뒤집은 다음 십진수 정수로 바꿔준다.
        # 그리고 마스킹을 해서, 만약 자릿수를 초과했다면 그 값은 제거될 수 있게 한다.
        result = int(''.join(result[::-1]), 2) & MASK

        # 음수 처리
        # 2의 보수에서 음수는 32번째 비트의 값, 즉 최상위 비트가 1인 경우이다.
        # 양의 정수 최댓값은 0x7FFFFFFF 이므로, 먄약 32번째 비트가 1이라면 이보다 큰 값이 되고, 이 경우 마스킹 값과 XOR 을 한 다음에 NOT 처리를 해서 다시 음수로 만들어준다.
        if result > INT_MAX:
            result = ~(result ^ MASK)

        return result

        # 간단한 버전
        # a 와 b의 역할을 구분해 a에는 carry 값을 고려하지 않는 a와 b의 합(sum)이 담기게 하고,
        # b에는 자릿수를 올려가며 carry 값이 담기게 했다.

        # while b != 0:
        #     a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
        #
        # if a > INT_MAX:
        #     a = ~(a ^ MASK)
        #
        # return a


# 13 / 13 test cases passed.
# Status: Accepted
# Runtime: 20 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 98.63 % of python3 submissions.
# Your memory usage beats 52.89 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.


