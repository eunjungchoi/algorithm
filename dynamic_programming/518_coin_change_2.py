# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
#
# Input: amount = 10, coins = [10]
# Output: 1
#
#
# Note:
#
# You can assume that
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
from typing import List


class Solution:
    """
    다른 액수의 화폐와 총 금액이 주어진다. 그 금액을 구성하는 조합의 수를 계산하는 함수를 작성하라. 각 종류의 동전을 무한정 가지고 있다고 가정한다.

    """

    def change(self, amount: int, coins: List[int]) -> int:

        """
        dynamic programming. tabulation:
        base case: 동전 없음 부터 시작해서 동전을 하나식 넣는다.
        추가된 각 코인에 대해 각 금액의 조합수를 0에서 타겟 금액으로 재귀적으로 계산한다.
        dp[0] = 1
        나머지는 모두 0에서 시작.
        모든 코인에 루프 적용
        각 코인데 대해 0부터 타겟금액 까지 모든 금액을 반복
        x의 각 양에 대해 dp[x] += dp[x-coin] 의 조합수를 계산

        """
        dp = [0] * (amount + 1)  # amount가 0일 때를 포함하기 위해.
        dp[0] = 1  # 0이 되는 경우의 수는 한 가지.

        for coin in coins:
            for price in range(coin, amount + 1):
                dp[price] += dp[price - coin]

        return dp[amount]


# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 128 ms
# Memory Usage: 14.5 MB
#
# Your runtime beats 98.91 % of python3 submissions.
# Your memory usage beats 37.71 % of python3 submissions.
