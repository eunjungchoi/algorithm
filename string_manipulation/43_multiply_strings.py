# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# 곱셈 계산기 만들기

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # return str(eval(num1) * eval(num2))

        result = [0] * (len(num1) + len(num2))

        for i, item1 in enumerate(reversed(num1)):  # 321
            for j, item2 in enumerate(reversed(num2)):  # 654
                result[i + j] += int(item1) * int(item2)
                result[i + j + 1] += result[i + j] // 10  # 10으로 나눠서 나온 몫은 carry. 위로 넘겨줌
                result[i + j] %= 10  # 해당인덱스에는 10으로 나눈 나머지만 삽입.

        while len(result) > 1 and result[-1] == 0:  # 결과물의 맨 앞에 위치할 0을 빼줌.
            result.pop()

        return ''.join(map(str, result[::-1]))  # result 를 뒤집고 str으로 치환후 join


# 311 / 311 test cases passed.
# Status: Accepted
# Runtime: 224 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 18.01 % of python3 submissions.
# Your memory usage beats 63.52 % of python3 submissions.
