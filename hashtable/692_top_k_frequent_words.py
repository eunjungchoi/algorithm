# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
import collections
import heapq
from typing import List


class Solution:
    """
    비어 있지 않은 단어 목록이 주어진다. 가장 빈도가 높은 k개까지 요소를 반환하라.
    가장 높은 빈도에서 가장 낮은 빈도로 분류되어야 한다.
    두 단어의 빈도가 같으면 알파벳 순서가 낮은 단어가 먼저다.
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        return [word for word, _ in sorted(count.items(), key=lambda x: (-x[1], x[0]))[:k]]
        # Time Complexity: O(N  log N), where N is the length of words.
        # We count the frequency of each word in O(N) time, then we sort the given words in O(N log N) time.
        # Space Complexity: O(N), the space used to store counter.



    def topKFrequent2(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        freqs = []
        for word, count in count.items():
            heapq.heappush(freqs, (-count, word))

        return [heapq.heappop(freqs)[1] for _ in range(k)]
        # Time Complexity:  O(N + k log N): our heapq.heapify operation and counting operations are O(N),
        # and each of k heapq.heappop operations are O(log N)
        # Space Complexity: O(N)O(N), the space used to store our count


# 110 / 110 test cases passed.
# Status: Accepted
# Runtime: 44 ms
# Memory Usage: 14.3 MB
#
# Your runtime beats 99.74 % of python3 submissions.
