# Given a string, your task is to count how many palindromic substrings in this string.
#
# The substrings with different start indexes or end indexes are counted as different substrings
# even they consist of same characters.
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
# Note:
#
# The input string length won't exceed 1000.
from typing import List


class Solution:
    def countSubstrings(self, s: str) -> int:

        # 1. expand around center.   O(n^2)
        # N = len(S)
        # ans = 0
        # for center in range(2*N - 1):
        #     left = center // 2
        #     right = left + center % 2
        #     while left >= 0 and right < N and S[left] == S[right]:
        #         ans += 1
        #         left -= 1
        #         right += 1
        # return ans

        # 2. manacher's algorithm
        def manacher(s: str) -> List:
            A = '@#' + '#'.join(s) + '#$'
            Z = [0] * len(A)  # palindrome_length_of each index. # 각 문자를 중심으로 한 팰린드롬 반지름을 인덱스 마다 저장

            center = right = 0

            for i in range(len(A) - 1):
                if i < right:  # 바로 앞의 팰린드롬에 포함된다는 것.
                    i_mirror = center - (i - center)  #
                    Z[i] = min(Z[i_mirror], right - i)
                    # i를 중심으로 하는 팰린드롬 반지름의 초기값.  center로부터 대칭되는 i_mirror의  팰린드롬 반지름과   right-i 를 비교해 더 작은 값이 초기값.

                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:  # # i를 중심으로 왼쪽 오른쪽 한칸씩 떨어진 값이 동일하면 팰린드롬을 확장시킴
                    Z[i] += 1  # 팰린드롬의 반지름을 1 증가

                # 기존의 right 경계를 벗어나면?  현재 인덱스를 중심으로 한 팰린드롬의 오른쪽끝이 새로운 right이 됨.
                if i + Z[i] > right:
                    # 이전의 max Center, right 값보다  현재 i 와 i를 중심으로 한 팰린드롬 반지름의 합이 더 크다면, center와 right을 현재 인덱스로 업데이트
                    center = i
                    right = i + Z[i]

            return Z

        return sum((length + 1) // 2 for length in manacher(s))
        # 사이사이에 #을 넣어서 길이를 두배로 만들어서 계산했기 때문에 팰린드롬의 직경이 각각 두배가 됐음. 다시 2로 나누어주고,  각각의 값들을 모두 합산.


# 130 / 130 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 96.72 % of python3 submissions.
# Your memory usage beats 39.62 % of python3 submissions.
