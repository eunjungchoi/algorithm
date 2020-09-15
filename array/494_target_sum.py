# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#
# Constraints:
#
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
import collections
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], Target: int) -> int:

        # 메모이제이션으로 풀이
        memo = {0: 1}  # target: path

        for num in nums:
            m = collections.defaultdict(int)
            for target, path in memo.items():
                m[target + num] += path
                m[target - num] += path
            memo = m

        return memo[Target]


# input: [1,1,1,1,1]
# output: 3

# 1 defaultdict(<class 'int'>, {1: 1, -1: 1})
# 1 defaultdict(<class 'int'>, {2: 1, 0: 2, -2: 1})
# 1 defaultdict(<class 'int'>, {3: 1, 1: 3, -1: 3, -3: 1})
# 1 defaultdict(<class 'int'>, {4: 1, 2: 4, 0: 6, -2: 4, -4: 1})
# 1 defaultdict(<class 'int'>, {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1})

# defaultdict(<class 'int'>, {5: 1, 3: 5, 1: 10, -1: 10, -3: 5, -5: 1})


# 139 / 139 test cases passed.
# Status: Accepted
# Runtime: 188 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 87.00 % of python3 submissions.
# Your memory usage beats 56.20 % of python3 submissions.
