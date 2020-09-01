# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using two pointers and sliding window
        max_length: int = 0
        start: int = 0
        used = {}

        for i, item in enumerate(s):
            if item in used and start <= used[item]:
                start = used[item] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[item] = i

        return max_length

#             string = []
#             if item not in string:
#                 string.append(item)
#             else:
#                 string = string[string.index(item)+1:]
#                 string.append(item)

#             max_length = max(max_length, len(string))


# 987 / 987 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 93.40 % of python3 submissions.
# Your memory usage beats 23.88 % of python3 submissions.
