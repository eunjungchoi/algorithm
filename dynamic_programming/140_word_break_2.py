# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
from typing import List


class Solution:
    """
    비어 있지 않은 문자열 s와 비어 있지 않은 단어 목록이 들어 있는 사전 단어Dict가 주어진다.
    s에 공백을 추가하여 각 단어가 유효한 사전 단어인 문장을 구성하라.
    가능한 모든 문장을 반환하라.

    참고:
    사전의 동일한 단어를 분할에서 여러 번 재사용할 수 있다.
    사전에 중복 단어가 포함되어 있지 않다고 가정할 수 있다.
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo) -> List:
        if not s:
            return []
        if s in memo:
            return memo[s]

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest = self.dfs(s[len(word):], wordDict, memo)
                for item in rest:
                    item = word + ' ' + item
                    res.append(item)

        memo[s] = res
        return res


# 36 / 36 test cases passed.
# Status: Accepted
# Runtime: 40 ms
# Memory Usage: 14.2 MB
#
# Your memory usage beats 29.69 % of python3 submissions.
# Your runtime beats 80.02 % of python3 submissions.

