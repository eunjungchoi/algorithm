# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 예외 처리. 음수면 바로 return False (-부호 때문에 palindrome이 될 수 없음)
        if x < 0:
            return False

        num = 1   # x와 같은 자릿수를 만들어줌.
        while x // num >= 10:  # x 나누기 num이 10의 배수 이상이면
            num *= 10  # num에 10을 곱해줌

        while x > 0:
            # x의 left와 right이 같은지 비교.
            left = x // num
            right = x % 10

            if left != right:
                return False

            # left와 right을 떼내고 가운데 숫자로 다시 x 설정
            x = (x % num) // 10
            num //= 100

        return True


# 11509 / 11509 test cases passed.
# Status: Accepted
# Runtime: 56 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 85.51 % of python3 submissions.
