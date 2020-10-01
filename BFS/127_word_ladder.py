# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:
#
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
from collections import defaultdict, deque
from typing import List


class Solution:
    """
        두 단어(beginWord 및 endWord)와 사전의 단어 목록이 주어진다.
        beginWord에서 endWord까지의 최단 변환 시퀀스의 길이를 찾아라

        1. 한 번에 한 글자만 변경할 수 있다.
        2. 각각의 변형된 단어들은 단어 목록에 존재해야 한다.

        이러한 변환 순서가 없으면 0을 반환하십시오.
        모든 낱말은 길이가 같다.
        모든 단어는 소문자 알파벳 문자만 포함한다.
        단어 목록에 중복되는 항목이 없다고 가정할 수 있다.
        beginWord와 endWord가 비어있지 않고, 같지 않다고 가정할 수 있다.
        """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 예외 처리
        if not endWord or endWord not in wordList or not beginWord or not wordList:
            return 0

        # 자료 구조
        length = len(beginWord)
        all_combo_dict = defaultdict(list)

        # 사전 만들기
        for word in wordList:
            for i in range(length):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        # queue for BFS
        queue = deque([(beginWord, 1)])  # 1 for the level
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.popleft()
            for i in range(length):
                # 현재 단어로 만들 수 있는 모든 중간 단어들을 순회하며,
                inter_word = current_word[:i] + "*" + current_word[i + 1:]
                # 그 중간 단어들과 딱 한글자만 다른 모든 단어를 순회하며
                for word in all_combo_dict[inter_word]:
                    if word == endWord:  # 도착 단어와 같으면 반환.
                        return level + 1

                    if word not in visited:  # 도착 단어가 아니고, 아직 방문하지 않았으면
                        visited[word] = True  # visited 목록에 추가하고
                        queue.append((word, level + 1))  # 큐에도 추가해둠.

                # all_combo_dict[inter_word] = []
        return 0


# 43 / 43 test cases passed.
# Status: Accepted
# Runtime: 116 ms
# Memory Usage: 17.4 MB
#
# Your runtime beats 90.74 % of python3 submissions.
# Your memory usage beats 25.24 % of python3 submissions.
