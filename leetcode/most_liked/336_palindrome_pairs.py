# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.
#
#
#
# Example 1:
#
# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:
#
# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:
#
# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
#
#
# Constraints:
#
# 1 <= words.length <= 5000
# 0 <= words[i] <= 300
# words[i] consists of lower-case English letters.
import collections
from typing import List

# brute force //

# class Solution:
#     def palindromePairs(self, words: List[str]) -> List[List[int]]:
#             def is_palindrome(word):
#                    return word == word[::-1]

#         output = []
#         for i, word1 in enumerate(words):
#             for j, word2 in enumerate(words):
#                 if i == j:
#                     continue
#                 if is_palindrome(word1 + word2):
#                     output.append([i, j])

#         return output


class TrieNode:
    def __init__(self):
        self.word_id = -1
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_word_ids = []


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, index: int, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, index: int, word: str) -> List[List[int]]:
        """
        Returns if the word is in the trie.
        """
        result = []
        node = self.root

        while word:
            # 판별로직 3: 탐색 중간에 word_id가 있고, 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]

        # 판별로직 1: 끝까지 탐색했을 때 word_id가 있는 경우
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 판별로직 2: 끝까지 탐색했을 때 palindrom_word_ids가 있는 경우
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = Trie()

        for i, word in enumerate(words):
            trie.insert(i, word)

        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))

        return results

# Runtime: 1044 ms, faster than 24.29% of Python3 online submissions for Palindrome Pairs.
# Memory Usage: 20.5 MB, less than 16.03% of Python3 online submissions for Palindrome Pairs.
