# Given a list of words (without duplicates),
# please write a program that returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.
from typing import List


class Solution:
    """
    중복되지 않은 단어 목록이 주어진다. 단어 목록에 있는 합성단어를 찾아서 모두 반환하는 프로그램을 작성하라.
    합성 단어는 주어진 배열에 있는 최소 두 개 이상의 짧은 단어로 이루어진 문자열로 정의된다.
    """

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        # DFS, memoization

        d = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]

            memo[word] = False

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    memo[word] = True
                    break
                if prefix in d and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in d and dfs(prefix):
                    memo[word] = True
                    break

            return memo[word]

        return [word for word in words if dfs(word)]


# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 484 ms
# Memory Usage: 36.2 MB
#
# Your runtime beats 68.99 % of python3 submissions.
# Your memory usage beats 10.90 % of python3 submissions.
