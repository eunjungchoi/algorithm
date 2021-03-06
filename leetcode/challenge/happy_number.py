# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process:
#  Starting with any positive integer, replace the number by the sum of the squares of its digits,
#  and repeat the process until the number equals 1 (where it will stay),
#  or it loops endlessly in a cycle which does not include 1.
#  Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0: return False
        if n == 1: return True

        number: int = n
        history: dict = {n: 1}

        while number != 1:
            nums = [int(x) for x in str(number)]
            result: int = 0

            for num in nums:
                result += num ** 2

            if result == 1:
                return True

            if result in history:
                return False
            else:
                history[result] = 1
                number = result


# 401 / 401 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 99.05 % of python3 submissions.
# Your memory usage beats 46.45 % of python3 submissions.

# after adding type:
# Your runtime beats 95.38 % of python3 submissions.
# Your memory usage beats 91.01 % of python3 submissions.

