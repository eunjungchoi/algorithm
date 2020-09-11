# Say you have an array prices for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
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

# 여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #   1. 기준값을 정해두고 가격이 오르면,  현재까지의 이익과 비교해  이번 가격과의 격차가 더 크면 현재까지의 이익 갱신.
        #         if len(prices) < 2: return 0

        #         default = prices[0]  # 기준 값 설정
        #         total_profit = 0
        #         current_profit = 0

        #         for i in range(1, len(prices)):
        #             if prices[i] > prices[i-1]:  # 가격이 오르면,  현재까지의 이익과 비교해  이번 가격과의 격차가 더 크면 현재까지의 이익 갱신.
        #                 if prices[i] - default > current_profit:
        #                     current_profit = prices[i] - default

        #             elif prices[i] < prices[i-1] :  # 가격이 떨어지면,  현재까지의 이익을 전체 이익에 합산하고 초기화.
        #                 default = prices[i]
        #                 total_profit += current_profit
        #                 current_profit = 0
        #                 continue

        #             if i == len(prices)-1:
        #                 total_profit += current_profit

        #         return total_profit

        #  2. greedy algorithm : 값이 오르는 경우에 매번 그리디 계산
        result = 0
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                result += prices[i+1] - prices[i]

        return result

        # 3. pythonic way
        # return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 15.1 MB
#
# Your runtime beats 99.07 % of python3 submissions.
# Your memory usage beats 79.49 % of python3 submissions.
