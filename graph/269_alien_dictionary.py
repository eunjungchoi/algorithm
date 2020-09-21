# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
#
# Example 1:
#
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
#
# Output: "wertf"
# Example 2:
#
# Input:
# [
#   "z",
#   "x"
# ]
#
# Output: "zx"
# Example 3:
#
# Input:
# [
#   "z",
#   "x",
#   "z"
# ]
#
# Output: ""
#
# Explanation: The order is invalid, so return "".
# Note:
#
# You may assume all letters are in lowercase.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.
from collections import defaultdict, Counter, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 1. BFS
        # 1) extracting as mush information about the alphabet order as we can out of the input word list
        # 2) representing that information in a meaningful way
        # 3) assembling a valid alphabet ordering

        # Step 0: create data structures + the in_degree of each unique letter to 0.
        # 자료구조 선언
        # 1 인접리스트 (set)
        # 2.들어오는 차수 counter
        adj_list = defaultdict(set)
        in_degree = Counter({char: 0 for word in words for char in word})

        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...

        # ["wrt","wrf","er","ett","rftt"]
        # ["wrf","er","ett","rftt"]
        # words 를 두 단어로 묶어서 비교하면서 인접리스트와 in_degree 딕셔너리 채우기
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:  # t != f
                    if d not in adj_list[c]:
                        adj_list[c].add(d)  # adj_list[t] = (f)
                        in_degree[d] += 1  # in_degree[f] += 1
                    break  # 다음 문자들은 비교할 필요 없음.

            # for 문이 break 되지 않고 끝까지 수행되면 else 문 실행.
            else:  # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""  # invalid case

        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.

        # in_degree 값이 0인 노드들을 queue에 집어넣고 빼면서 output에 차곡차곡 쌓기
        output = []
        queue = deque([char for char in in_degree if in_degree[char] == 0])  # deque : popleft() 시간복잡도가 O(1)

        while queue:
            char = queue.popleft()
            output.append(char)

            for d in adj_list[char]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""

        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)


# 119 / 119 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.9 MB
#
# Your runtime beats 81.45 % of python3 submissions.
# Your memory usage beats 34.53 % of python3 submissions.
