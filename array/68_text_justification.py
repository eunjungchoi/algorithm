# Given an array of words and a width maxWidth,
# format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words,
# the empty slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# Note:
#
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.
# Example 1:
#
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Example 2:
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.
# Example 3:
#
# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current = []
        length = 0

        for word in words:
            if length + len(current) + len(word) > maxWidth:
                spaces = maxWidth - length
                if len(current) == 1:
                    result.append(current[0] + ' ' * spaces)
                else:
                    space_in_words, extra_spaces = divmod(spaces, len(current) - 1)
                    for i in range(extra_spaces):  # 여백을 골고루 분배 후에 남은 여백은 왼쪽부터 분배하기
                        current[i] += ' '
                    result.append((' ' * space_in_words).join(current))
                current = []
                length = 0

            current.append(word)
            length += len(word)

        return result + [' '.join(current).ljust(maxWidth)]


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 14.2 MB
#
# Your runtime beats 64.97 % of python3 submissions.
