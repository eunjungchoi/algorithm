# A string S of lowercase English letters is given.
# We want to partition this string into as many parts as possible so that each letter appears in at most one part,
# and return a list of integers representing the size of these parts.
#
#
#
# Example 1:
#
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
#
#
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # greedy algorithm
        last = {char: i for i, char in enumerate(S)}  # 특정 문자가 등장하는 마지막 인덱스로 업데이트
        start = 0
        group_last_index = 0
        result = []

        for i, char in enumerate(S):
            group_last_index = max(group_last_index, last[char])  # 순회하면서 (한 배를 탄) 각 알파벳의 최후 인덱스로 업데이트

            if i == group_last_index:  # 현재 인덱스가 현재 알파벳의 마지막 인덱스와 같으면 여기서 끊고 result에 추가
                result.append(group_last_index - start + 1)
                start = i + 1  # 새로운 문자열을 시작할 파티션을 i+1로 설정.

        return result

# 116 / 116 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Memory Usage: 13.9 MB

# Your runtime beats 86.87 % of python3 submissions.
# Your memory usage beats 30.39 % of python3 submissions.
