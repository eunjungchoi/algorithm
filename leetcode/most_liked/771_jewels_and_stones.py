# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
import collections


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # using defaultdict
        # freqs = collections.defaultdict(int)
        # count = 0
        #
        # for i in S:
        #     freqs[i] += 1
        #
        # for i in J:
        #     count += freqs[i]
        # return count

        # using Counter
        # count = 0
        # freqs = collections.Counter(S)
        # for c in J:
        #     count += freqs[c]
        # return count

        # pythonic way
        return sum(i in J for i in S)


# 254 / 254 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Memory Usage: 13.8 MB
#
# Your runtime beats 84.71 % of python3 submissions.
# Your memory usage beats 81.50 % of python3 submissions.
# <파이썬 알고리즘 인터뷰> 참고.
# 세 방법 모두 속도는 비슷.

