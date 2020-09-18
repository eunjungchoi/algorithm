# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example 1:
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """Naive recursive solution ==> timeout error """
        # if not word1 and not word2:
        #     return 0
        # if not word1:
        #     return len(word2)
        # if not word2:
        #     return len(word1)
        #
        # if word1[0] == word2[0]:
        #     return self.minDistance(word1[1:], word2[1:])
        #
        # insert = 1 + self.minDistance(word1, word2[1:])
        # delete = 1 + self.minDistance(word1[1:], word2)
        # replace = 1 + self.minDistance(word1[1:], word2[1:])
        # return min(insert, replace, delete)

        """Dynamic programming solution"""
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            table[i][0] = i
        for j in range(n + 1):
            table[0][j] = j
        #       r,  o,  s
        # [ [0, 1, 2, 3],
        # [  1h, 1, 2, 3],
        # [  2o, 2, 1, 2],
        # [  3r, 2, 2, 2],
        # [  4s, 3, 3, 2],
        # [  5e, 4, 4, 3] ]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    table[i][j] = table[i - 1][j - 1]
                else:
                    table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])

        return table[-1][-1]


# 1146 / 1146 test cases passed.
# Status: Accepted
# Runtime: 184 ms
# Memory Usage: 17.4 MB
#
# Your runtime beats 76.04 % of python3 submissions.
# Your memory usage beats 48.31 % of python3 submissions.

