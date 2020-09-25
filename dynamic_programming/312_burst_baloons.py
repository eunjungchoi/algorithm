# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# Example:
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
from functools import lru_cache
from typing import List


class Solution:
    # dynamic programming: Top down
    # caching results / recursive calls
    def maxCoins1(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        # cache this
        @lru_cache(None)    # cache 하지 않으면 timeout error
        def dp(left, right):
            # no more ballons can be added
            if left + 1 == right:
                return 0

            list_ = [nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left + 1, right)]
            return max(list_)

        return dp(0, len(nums) - 1)

    # dynamic programming: bottom up
    def maxCoins2(self, nums: List[int]) -> int:
        # 0에서 n-1까지 인덱스가 붙은 n개의 풍선이 있다. 각각의 풍선은 인덱스 숫자가 그려져있다.
        # 모든 풍선을 터트려야 한다. 풍선 i 번째를 터트리면 num[left] * nums[i] * nums[right] coin 을 얻는다.
        # 터트리고 나면 left와 right 이 인접한다.
        # 얻을 수 있는 최대의 coin을 구하라.

        # 가장 작은 숫자부터
        # 루프 돌면서 heap에 집어넣고 제일 작은 수 부터 뽑아서 터트리기

        # reframe problem as before

        # dynamic programming
        
        nums = [1] + nums + [1]
        n = len(nums)

        # dp will store the results of our calls
        dp = [[0] * n for _ in range(n)]

        # iterate over dp and incrementally build up to dp[0][n-1]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                # same formula to get the best score from (left, right) as before
                dp[left][right] = max(
                    nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right))

        return dp[0][n - 1]


# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 308 ms
# Memory Usage: 14.4 MB
#
# Your runtime beats 98.99 % of python3 submissions.
# Your memory usage beats 40.14 % of python3 submissions.
