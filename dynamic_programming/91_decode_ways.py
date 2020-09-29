# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: s = "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: s = "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:
#
# Input: s = "0"
# Output: 0
# Example 4:
#
# Input: s = "1"
# Output: 1
# Example 5:
#
# Input: s = "2"
# Output: 1
#
#
# Constraints:
#
# 1 <= s.length <= 100
# s contains only digits and may contain leading zero(s).


class Solution:
    """
    A-Z의 문자가 포함된 메시지를 다음 매핑을 사용하여 숫자로 인코딩한다.
    숫자만 포함하는 비어 있지 않은 문자열이 있을 경우, 해당 문자열을 디코딩하는 총 방법 수를 결정하라.
    정답은 32비트 정수에 맞도록 보장된다.
    """

    def numDecodings(self, s: str) -> int:
        # dynamic programming
        # 1 -> A로 한자리 디코딩, 또는 25 -> Y 로 두자리 디코딩이 될 수 있음.
        # 유효하다면 나머지를 해독하기 위해 앞으로 계속 나아감.
        if not s:
            return 0

        dp = [0] * (len(s) + 1)

        # base case initialization
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1

        # s[i] == dp[i+1]
        # dp[i]:s[:i] 를 디코딩하는 방법 수
        # dp[i] = dp[i-1] + dp[i-2]
        # 항상 맞는 것은 아님. 디코드가 가능할 때만 이전 지수의 결과를 추가. 바톤은 디코딩 가능성에 따라 다음 인덱스로 전달되거나 전달되지 않음

        for i in range(1, len(s)):
            # 1 step jump. check if successful single digit decode is possible.
            if s[i] != '0':
                dp[i + 1] += dp[i]

            # 2 step jump. check if successful two digit decode is possible.
            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]

        return dp[-1]

        # time complexity: O(N). N is length of the string.
        # space complexity: O(N). the length of the DP array.


# 268 / 268 test cases passed.
# Status: Accepted
# Runtime: 24 ms
# Memory Usage: 14.2 MB
# 
# Your runtime beats 97.85 % of python3 submissions.
# Your memory usage beats 31.12 % of python3 submissions.
