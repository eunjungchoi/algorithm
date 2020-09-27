# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # brute force ==> timeout error
        # 0부터 n-1 번째 까지 순회하면서  자기를 뺀 string이 회문인지 체크
        #         new_a = []
        #         for i in range(len(s)):
        #             new_a = s[:i] + s[i+1:]
        #             if new_a == new_a[::-1]:
        #                 return True

        #         return False

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
        return True


# Time: O(n)
# Space: O(n)

# 460 / 460 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Memory Usage: 14.6 MB
#
# Your runtime beats 91.97 % of python3 submissions.
# Your memory usage beats 9.72 % of python3 submissions.
