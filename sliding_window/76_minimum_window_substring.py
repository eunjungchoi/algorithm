# Given a string S and a string T,
# find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

# 문자열 S, T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라.
# 브루트 포스로 풀면 O(n^2) 으로 타임아웃 에러를 일으킨다.
# 이런 유형의 문제는 투 포인터를 사용하면 O(n^2) -> O(n)으로 줄일 수 있다.
# 계속 우측으로 이동하는 슬라이딩 윈도우이면서 적절한 위치를 찾았을 때 좌우 포인터의 크기를 좁혀 나가는 투 포인터로 풀이할 수 있을 것 같다.


import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)  # 필요한 문자 각각의 개수
        missing = len(t)  # 필요한 문자의 전체 개수
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):  # 1부터 시작. 오른쪽 포인터의 값은 계속 늘려나간다.
            missing -= need[char] > 0
            # 현재 문자가, 필요한 문자 need[char]에 포함되어 있으면 필요한 문자의 전체 개수인 Missing을 1 감소시킴
            need[char] -= 1  # 해당 문자의 필요한 개수 need[char] 도 1 감소 시킴

            # 필요한 문자의 개수가 0이 되면,  왼쪽 포인터를 더 줄일 수 있는지 체크 (기준: 음수)

            if missing == 0:
                # 왼쪽 포인터가 불필요한 문자를 가리키고 있다면 분명 음수일 것.
                # 0을 가리키는 위치까지 왼쪽 포인터를 이동한다.
                # 슬라이딩 윈도우의 크기가 점점 더 줄어드는 형태

                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                # need[s[left]] 가 0이 될 때까지의 왼쪽 포인터를 정답으로 간주.
                # 더 작은 값을 찾을 때까지 유지하다가 가장 작은 값인 경우, 정답으로 슬라이싱 결과를 리턴

                if not end or right - left <= end - start:
                    start, end = left, right

                need[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


# 268 / 268 test cases passed.
# Status: Accepted
# Runtime: 104 ms
# Memory Usage: 14.5 MB
#
# Your runtime beats 88.27 % of python3 submissions.
# Your memory usage beats 55.03 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
