# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like
# (i.e., buy one and sell one share of the stock multiple times).
#
# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Example 2:
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
# Constraints:
#
# 1 <= prices.length <= 3 * 10 ^ 4
# 0 <= prices[i] <= 10 ^ 4

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        default = prices[0]
        total_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                if prices[i] - default > current_profit:
                    current_profit = prices[i] - default
            elif prices[i] < prices[i - 1]:
                default = prices[i]
                total_profit += current_profit
                current_profit = 0
                continue
            if i == len(prices) - 1:
                total_profit += current_profit
                current_profit = 0

        return total_profit


# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 60 ms
# Memory Usage: 15.1 MB

# Your runtime beats 88.63 % of python3 submissions.
# Your memory usage beats 68.83 % of python3 submissions.
