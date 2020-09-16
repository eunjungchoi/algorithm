# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dynamic programming : tabulation (bottom-up)

        memo = [0] + [float('inf') for i in range(amount)]   # array에 amount 만큼 칸을 만들고 각각 최댓값을 미리 넣어놓음.

        for i in range(1, amount + 1):  # [1,2,3,4,5,6,7,8,9,10,11] 1부터 시작해서 amount 숫자만큼 순회함
            for coin in coins:
                if i - coin >= 0:   # partial amount가 coin보다 크면
                    memo[i] = min(memo[i], memo[
                        i - coin] + 1)  # dp의 원래 값 dp[i]와  dp[i-coin] 값을 비교해 더 작은 것으로 업데이트.  dp[0]을 초기값으로 해서 점점 채워짐

        if memo[-1] == float('inf'):  # 마지막 값 (=amount) 값이 여전히 무한대이면, 답이 없다는 것.
            return -1

        return memo[-1]


#         # greedy algorithm 으로 안 풀림.

#         coins.sort(reverse=True)
#         count = 0

#         for coin in coins:
#             while amount > 0:
#                 if amount - coin < 0:
#                     break
#                 amount -= coin
#                 count += 1

#         if amount > 0 or count == 0:
#             return -1
#         return count


# 182 / 182 test cases passed.
# Status: Accepted
# Runtime: 1584 ms
# Memory Usage: 14.1 MB
#
# Your runtime beats 51.33 % of python3 submissions.
# Your memory usage beats 43.24 % of python3 submissions.
