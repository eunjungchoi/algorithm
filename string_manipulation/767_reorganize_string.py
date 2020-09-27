# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
#
# If possible, output any possible result.  If not possible, return the empty string.
#
# Example 1:
#
# Input: S = "aab"
# Output: "aba"
# Example 2:
#
# Input: S = "aaab"
# Output: ""
# Note:
#
# S will consist of lowercase letters and have length in range [1, 500].


class Solution:
    """
    문자열이 S인 경우 인접한 두 문자가 같지 않도록 문자를 다시 정렬할 수 있는지 확인하십시오.
    가능한 경우 가능한 결과를 출력하십시오. 불가능할 경우 빈 문자열을 반환하십시오.
    """

    def reorganizeString(self, S: str) -> str:
        """
        홀수 인덱스에 최소 공통 문자를 넣고 짝수 인덱스(빈도 순서에 따라 왼쪽에서 오른쪽으로 모두)에 가장 일반적인 문자를 넣는다. 어떤 문자가 너무 자주 나타날 경우에만 작업이 불가능하며, 이 경우 모든 짝수 인덱스와 최소한 마지막 홀수 인덱스를 차지하게 되므로 마지막 두 인덱스를 체크한다.
        """
        a = sorted(sorted(S), key=S.count)
        half = len(S) // 2

        a[1::2], a[::2] = a[:half], a[half:]
        if a[-1] == a[-2]:
            return ''

        return ''.join(a)


# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 14.1 MB

# Your runtime beats 89.86 % of python3 submissions.
